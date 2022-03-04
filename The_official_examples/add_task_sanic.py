# -*- coding: utf-8 -*-

import asyncio

from sanic import Sanic, response

app = Sanic("Example")


async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print("Server successfully started!")


app.add_task(notify_server_started_after_five_seconds())


@app.route("/")
async def test(request):
    return response.json({"test": True})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
