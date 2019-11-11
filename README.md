#  Bot_ML

## Для решения этой задачи была применена сверточная нейросеть, архитектура которой представлена ниже
```
_________________________________________________________________
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 44, 44, 128)       18944     
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 22, 22, 128)       0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 18, 18, 256)       819456    
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 9, 9, 256)         0         
_________________________________________________________________
flatten (Flatten)            (None, 20736)             0         
_________________________________________________________________
dense (Dense)                (None, 1024)              21234688  
_________________________________________________________________
dense_1 (Dense)              (None, 512)               524800    
_________________________________________________________________
dense_2 (Dense)              (None, 256)               131328    
_________________________________________________________________
dropout (Dropout)            (None, 256)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 25)                6425      
=================================================================
Total params: 22,735,641
Trainable params: 22,735,641
Non-trainable params: 0
_________________________________________________________________
```

## Запуск бота
```
python main.py
```
## Cсылка
[Bot Machine Learning](https://t.me/ML_123_bot)

## Пример работы бота
![Label Tool](bot_test.jpg)
