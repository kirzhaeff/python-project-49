install:
		poetry install
brain-games:
		poetry run brain-games
build: #сборка пакетов
		poetry build
publish:
		poetry publish --dry-run
package-install: #установка пакетов
		python3 -m pip install dist/*.whl
package-reinstall:
		python3 -m pip install dist/*.whl --force-reinstall
