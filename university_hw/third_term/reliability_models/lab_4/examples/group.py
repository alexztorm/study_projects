from flask import render_template
from flask import request


class group:
	def f(self):
		return render_template("asm2304/st04/index.html", s="asm2304.st04.group.f()", selfurl='/'+request.url_rule.rule.split('/')[1])
