from sanic import Sanic
from sanic.response import json

app = Sanic('aa')

from cyberbrain import trace
# 异步响应:

@app.route("/")
@trace
async def qtest(request):
    return json({"test": True})


app.run(host="0.0.0.0", port=8003)
