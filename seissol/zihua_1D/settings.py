from pathlib import Path

import numpy as np

from components import general_settings
from . import builder

# ==================================================================================================
parallel_run_settings = general_settings.ParallelRunSettings(
    num_chains=4,
    chain_save_path=Path("results_seissol_zihua_1D/chain"),
    chain_load_path=None,
    node_save_path=Path("results_seissol_zihua_1D/final_node"),
    node_load_path=Path("results_seissol_zihua_1D/final_node"),
    rng_state_save_path=None,
    rng_state_load_path=None,
    overwrite_chain=True,
    overwrite_node=True,
    overwrite_rng_states=True,
)

sampler_setup_settings = general_settings.SamplerSetupSettings(
    num_levels=2,
    subsampling_rates=[5, -1],
    max_tree_height=50,
    underflow_threshold=-1000,
    rng_seed_mltree=1,
    rng_seed_node_init=2,
    mltree_path=None,
)

sampler_run_settings = general_settings.SamplerRunSettings(
    num_samples=3,
    initial_state=None,
    num_threads=4,
    print_interval=1,
    tree_render_interval=1,
)

logger_settings = general_settings.LoggerSettings(
    do_printing=True,
    logfile_path=Path("results_seissol_zihua_1D") / Path("mtmlda"),
    debugfile_path=Path("results_seissol_zihua_1D") / Path("mtmlda_debug"),
    write_mode="w",
)

# --------------------------------------------------------------------------------------------------
inverse_problem_settings = builder.InverseProblemSettings(
    prior_intervals=np.array(
        [
            [1e6, 9e6],
        ]
    ),
    prior_rng_seed=3,
    ub_model_configs=({"order": 4}, {"order": 5}),
    ub_model_address="http://localhost:4242",
    ub_model_name="forward",
    use_surrogate=False,
    ub_surrogate_address="http://localhost:4243",
    ub_surrogate_name="surrogate",
)

sampler_component_settings = builder.SamplerComponentSettings(
    proposal_step_width=0.5,
    proposal_covariance=1e12 * np.identity(1),
    proposal_rng_seed=4,
    accept_rates_initial_guess=[0.5, 0.8],
    accept_rates_update_parameter=0.01,
)

initial_state_settings = builder.InitialStateSettings()
