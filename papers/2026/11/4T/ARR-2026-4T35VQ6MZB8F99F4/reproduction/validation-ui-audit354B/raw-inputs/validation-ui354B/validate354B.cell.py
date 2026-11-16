# Sole validation entrypoint. Existing runner owns all normal/-O tests and actual checks.
# Run only after the previous materializer has actually succeeded. Do not rerun into existing output.
read_exit((UI/'input-materialization354B').with_suffix('.exit'),require_success=True)
validation_child=observed_child354B('run_validation354A.py','validation-run354B',3600)
print(json.dumps(validation_child))
