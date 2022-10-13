python -m my_omnipose --train --use_gpu --dir /home/DataSet/Omnipose_raw --mask_filter _label --n_epochs 300 \
--pretrained_model cyto2_omni --train_size --chan 2 --chan2 3 --learning_rate 1e-4 --diameter 0 --batch_size 8 --RAdam \
--save_every 1 --min_train_masks 1