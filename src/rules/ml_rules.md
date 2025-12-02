## ML Rules for FPS

- **Data integrity first**: All datasets must include explicit schema definitions and validation steps before modeling.
- **Reproducible pipelines**: Any experiment must be reproducible via scripted steps (no notebook-only logic).
- **Train/val/test separation**: Never tune hyperparameters or features on the test set.
- **Explainability**: Prefer models and features that can be explained to a non-ML stakeholder.
- **Version everything**: Datasets, models, and configuration should be versioned or at least checksumed.


