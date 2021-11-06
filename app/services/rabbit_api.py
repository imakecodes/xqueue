import subprocess
import os

from requests import Session, ConnectionError
import psutil


class RabbitApi:
    _queues = None

    def __init__(self):

        self.base_url = "http://{RABBITMQ_HOST}:{RABBITMQ_ADMIN_PORT}".format(
            **{
                "RABBITMQ_HOST": os.getenv("RABBITMQ_HOST", "localhost"),
                "RABBITMQ_ADMIN_PORT": os.getenv("RABBITMQ_ADMIN_PORT", "15672"),
            }
        )
        self.base_api = "/".join([self.base_url, "api"])
        self.vhost = os.getenv("RABBITMQ_VHOST", "/")
        self.session = Session()
        self.session.auth = (os.getenv("RABBITMQ_USER", "guest"), os.getenv("RABBITMQ_PASSWORD", "guest"))

    def queue_create(self, queue_name, durable=True, auto_delete=False, *args, **kwargs):
        payload = kwargs
        payload["durable"] = durable
        payload["auto_delete"] = auto_delete
        try:
            response = self.session.put(url="/".join([self.base_api, "queues", self.vhost, queue_name]), json=payload)
            response.raise_for_status()
        except ConnectionError as e:
            return False

        return True

    def queue_delete(self, queue_name):
        try:
            response = self.session.delete(url="/".join([self.base_api, "queues", self.vhost, queue_name]))
            response.raise_for_status()
        except ConnectionError as e:
            return False
        return True

    def queue_purge(self, queue_name):
        try:
            response = self.session.delete(url="/".join([self.base_api, "queues", self.vhost, queue_name, "contents"]))
            response.raise_for_status()
        except ConnectionError as e:
            return False
        return True

    def load_queues_info(self):
        try:
            response = self.session.get(url="/".join([self.base_api, "queues"]))
            response.raise_for_status()
        except ConnectionError as e:
            return False
        self._queues = response.json()

    def queue_info(self, queue_name):
        for queue in self._queues:
            if not queue["vhost"] == self.vhost:
                continue

            if queue["name"] == queue_name:
                return queue
        return {
            "consumers": 0,
            "messages_unacknowledged": 0,
            "messages_unacknowledged_details": {
                "rate": 0,
            },
            "messages": 0,
            "messages_details": {
                "rate": 0,
            },
        }

    def consumer_info(self, queue_name):
        response = {
            "processes": [],
        }
        attrs = [
            "pid",
            "name",
            "cmdline",
            "cpu_percent",
            "create_time",
        ]

        for proc in psutil.process_iter(attrs=attrs):
            cmdline = proc.info["cmdline"]
            if isinstance(cmdline, list):
                command = " ".join(cmdline)
                if "celery" not in command:
                    continue
                if queue_name not in command:
                    continue
                response["processes"].append(proc.info)
        response["workers"] = len(response["processes"])
        return response

    def queue_url(self, queue_name):
        return "/".join(
            [
                self.base_url,
                "#",
                "queues",
                self.vhost,
                queue_name,
            ]
        )
