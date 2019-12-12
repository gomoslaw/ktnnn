
retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/inception_resnet_v2/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/inception_resnet_v2/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/inception_resnet_v2/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/inception_resnet_v2/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/inception_resnet_v2/model/ \
--checkpoint_path /home/michal/notebooks/retrain/inception_resnet_v2/checkpoint_path/


retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/resnet_v1_101/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/resnet_v1_101/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/_resnet_v1_101/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/resnet_v1_101/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/resnet_v1_101/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/resnet_v1_101/model/ \
--checkpoint_path /home/michal/notebooks/retrain/resnet_v2_101/checkpoint_path/

retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/resnet_v2_152/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/resnet_v2_152/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/_resnet_v2_152/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/resnet_v2_152/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/resnet_v2_152/model/ \
--checkpoint_path /home/michal/notebooks/retrain/resnet_v2_152/checkpoint_path/


retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/inception_v1/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/inception_v1/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/inception_v1/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/inception_v1/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/inception_v1/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/inception_v1/model/ \
--checkpoint_path /home/michal/notebooks/retrain/inception_v1/checkpoint_path/A


retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/inception_v2/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/inception_v2/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/inception_v2/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/inception_v2/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/inception_v2/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/inception_v2/model/ \
--checkpoint_path /home/michal/notebooks/retrain/inception_v2/checkpoint_path/



retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/inception_v3/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/inception_v3/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/inception_v3/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/inception_v3/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/inception_v3/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/inception_v3/model/ \
--checkpoint_path /home/michal/notebooks/retrain/inception_v3/checkpoint_path/


retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/mobilenet_v2/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/mobilenet_v2/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/mobilenet_v2/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/mobilenet_v2/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/mobilenet_v2/model/ \
--checkpoint_path /home/michal/notebooks/retrain/mobilenet_v2/checkpoint_path/

retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/mobilenet_v1/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/mobilenet_v1/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/mobilenet_v1/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/mobilenet_v1/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/mobilenet_v1/feature_vector/3 \
--saved_model_dir /home/michal/notebooks/retrain/mobilenet_v1/model/ \
--checkpoint_path /home/michal/notebooks/retrain/mobilenet_v1/checkpoint_path/

retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/nasnet/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/nasnet/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/nasnet/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/nasnet/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/nasnet_large/feature_vector/3\
--saved_model_dir /home/michal/notebooks/retrain/nasnet/model/ \
--checkpoint_path /home/michal/notebooks/retrain/nasnet/checkpoint_path/

retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/pnasnet/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/pnasnet/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/pnasnet/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/pnasnet/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/3\
--saved_model_dir /home/michal/notebooks/retrain/pnasnet/model/ \
--checkpoint_path /home/michal/notebooks/retrain/pnasnet/checkpoint_path/

retrain.py \
--image_dir /home/michal/notebooks/retrain/dataset \
--output_graph  /home/michal/notebooks/retrain/amoebanet/output_graph.pb \
--output_labels /home/michal/notebooks/retrain/amoebanet/labels.txt \
--summaries_dir /home/michal/notebooks/retrain/amoebanet/retrain_logs \
--bottleneck_dir /home/michal/notebooks/retrain/amoebanet/bottleneck_dir \
--tfhub_module  https://tfhub.dev/google/imagenet/amoebanet_a_n18_f448/classification/1\
--saved_model_dir /home/michal/notebooks/retrain/amoebanet/model/ \
--checkpoint_path /home/michal/notebooks/retrain/amoebanet/checkpoint_path/


