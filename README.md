# Automated Unit Testing in a CI Pipeline (DevOps)

A small Python project that shows how unit tests run **automatically** on every
`git push` / pull request using a CI pipeline (GitHub Actions, plus an
equivalent Jenkinsfile).

## Project structure
```
ci-unit-testing/
├── app/calculator.py              # code under test
├── tests/test_calculator.py       # pytest unit tests
├── requirements.txt               # pytest, pytest-cov
├── pytest.ini                     # test + coverage settings (fail under 80%)
├── .github/workflows/ci.yml       # GitHub Actions pipeline
└── Jenkinsfile                    # Jenkins pipeline (alternative)
```

## Run locally
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Run in CI (GitHub Actions)
1. Create a GitHub repo and push this folder:
   ```bash
   git init && git add . && git commit -m "Add unit tests and CI"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
2. Open the **Actions** tab. The "CI - Unit Tests" workflow runs automatically.
3. Python 3.10, 3.11 and 3.12 run in parallel (matrix build).
4. Test report (`test-results.xml`) and `coverage.xml` are saved as artifacts.

## Demo: show the pipeline catching a bug
1. In `app/calculator.py` change `return a + b` to `return a - b`.
2. Commit and push. The pipeline turns RED and the build fails.
3. Revert the change, push again. The pipeline turns GREEN.

## Pipeline flow
Push code -> Checkout -> Set up Python -> Install dependencies -> Run pytest
-> Check coverage (>= 80%) -> Upload reports -> Pass / Fail
