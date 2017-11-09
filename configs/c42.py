import numpy as np
height = 288
width = 512
batch_size = 10
initial_learning_rate = 2e-4
theta_mul = 400
regu_mul = 30
img_mul = height * width * 1
temp_mul = height * width * 3
black_mul = 10000
training_iter = 200000#70000
step_size = 60000#30000
train_data_size = 27000#4000
test_data_size = 2500#600
crop_rate = 1
before_ch = 7
after_ch = 7
tot_ch = before_ch + after_ch + 1
test_batches = 10
random_crop_rate = 0.9
disp_freq = 50
test_freq = 500
save_freq = 1000
no_theta_iter = 1000000
do_temp_loss_iter = 5000
do_theta_10_iter = -1
do_black_loss_iter = 1000
do_theta_only_iter = 300
tfrecord_item_num = 10
log_dir = 'log/42/'
model_dir = 'models/42/'
data_dir = 'data5/'
rand_H_max = np.array([[1.1, 0.1, 0.5], [0.1, 1.1, 0.5], [0, 0, 1]])
rand_H_min = np.array([[0.9, -0.1, -0.5], [-0.1, 0.9, -0.5], [0, 0, 1]])
