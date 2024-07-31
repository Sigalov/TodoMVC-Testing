
# TodoMVC Testing

This repository contains automated E2E tests for the TodoMVC application using Selenium 4 and pytest.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests, use the following command:
```bash
cd tests
pytest
```

## Additional Information

- The tests are located in the `tests` directory.
- Tests can be executed in parallel using the `pytest-xdist` plugin by adding the `-n` option, e.g., `pytest -n 4` to run tests on 4 CPUs.

## Pytest Configuration

The `pytest.ini` file includes the following configurations:
- `testpaths = tests`: Specifies the directory where tests are located.
- `norecursedirs = .git`: Excludes the `.git` directory from test discovery.

### Marks

The project uses various pytest markers to categorize tests:
- `add`: Tests related to adding items
- `edit`: Tests related to editing items
- `complete`: Tests related to completing items
- `delete`: Tests related to deleting items
- `toggle`: Tests related to toggling item status
- `filter`: Tests related to filtering items
- `count`: Tests related to counting items

### Using Marks

To run tests with a specific mark, use the `-m` option followed by the mark name. For example, to run tests related to adding items, use the following command:

```bash
pytest -m add
```

