python -m my_omnipose --dir /home/DataSet/CellSeg/TuningSet \
--pretrained_model /home/DataSet/Omnipose_rgb/models/cellpose_residual_on_style_on_concatenation_off_omni_Omnipose_rgb_2022_10_07_14_32_14.659748 \
--pretrained_size --use_gpu --chan 2 --chan2 3 --diameter 0 --save_tif --no_npy \
--savedir ./outputs