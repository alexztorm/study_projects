from flask import request


class WebIO:
    @staticmethod
    def input(field):
        return request.form.get(field)

    @staticmethod
    def output(text):
        return text
