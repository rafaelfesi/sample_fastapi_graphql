from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema import schema

# FastAPIのインスタンスを作成
app = FastAPI()

# GraphQLを提供するためのエンドポイントを定義
app.add_route("/", GraphQLApp(schema=schema))