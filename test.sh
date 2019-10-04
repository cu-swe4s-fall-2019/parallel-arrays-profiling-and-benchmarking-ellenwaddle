test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_pycodestyle_gtex pycodestyle plot_gtex.py
assert_exit_code 0

run test_pcs_dv pycodestyle data_viz.py
assert_exit_code 0

run test_pcs_tdv pycodestyle test_data_viz.py
assert_exit_code 0
