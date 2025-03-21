# https://docs.docker.com/engine/reference/builder/

FROM python:3.12
COPY dist/*.whl .
RUN pip install *.whl
# Ejecuta la función main() del módulo controller.kafka_app
CMD ["python", "-m", "autogen_team.controller.kafka_app"]

