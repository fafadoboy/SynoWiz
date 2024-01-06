#!/usr/bin/env python3

import connexion

if __name__ == "__main__":
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api(
        "swagger.yaml",
        arguments={"title": "API for managing practice sets and their executions"},
    )
    app.run(host="0.0.0.0", port=80)
