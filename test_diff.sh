git init
git add src/autogen_team/core/schemas.py
git commit -m "initial commit"
echo "# test" >> src/autogen_team/core/schemas.py
python3 scripts/doc_updater.py diff
