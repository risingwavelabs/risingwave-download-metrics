# RisingWave Download Metrics

- `index.html` provides the dashboard. You may test it by uncommenting `test_data` inside, then `open index.html`.
  It just uses charts.js.
- The git branch `data` contains the data files. Please don't push to it manually, unless you know what you're doing.
- We use github actions, see `.github/workflows/update-counts.yaml` for workflow steps.
- `update_data.py` is used to update the `counts.json` file in the `data` branch. Used in the actions workflow.
