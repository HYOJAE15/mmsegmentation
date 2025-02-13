# Copyright (c) OpenMMLab. All rights reserved.
from .inference import inference_segmentor, init_segmentor, show_result_pyplot, inference_segmentor_sw, save_result_palette
from .test import multi_gpu_test, single_gpu_test
from .train import (get_root_logger, init_random_seed, set_random_seed,
                    train_segmentor)

__all__ = [
    'get_root_logger', 'set_random_seed', 'train_segmentor', 'init_segmentor',
    'inference_segmentor', 'inference_segmentor_sw', 'multi_gpu_test', 'single_gpu_test',
    'show_result_pyplot', 'init_random_seed', 'save_result_palette'
]
