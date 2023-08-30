1) I initially used a **Sequential Model** with a **single** convolutional layer that had **32** filters. I paired this with a **single** max pooling layer with a pool size of **(2, 2)** and a final output layer. This yielded an accuracy of roughly **92.8%** which I felt could be improved.
   `333/333 - 1s - loss: 0.8380 - accuracy: 0.9278 - 1s/epoch - 3ms/step`

2) I then added a **Hidden Layer** with **128** neurons but only achieved an accuracy of **92.0%** which was not an improvement on the initial model.
   `333/333 - 1s - loss: 0.5166 - accuracy: 0.9200 - 969ms/epoch - 3ms/step`

3) I considered the idea of overfitting and so I added a dropout of **0.5**. This dramatically reduced my accuracy to approximately **5.48%** and so I decided my previous results were likely a result of overfitting.
   `333/333 - 1s - loss: 3.4943 - accuracy: 0.0548 - 1s/epoch - 3ms/step`

4) I decided that if overfitting was the problem, I needed to generalise the data more and so I added another convolutional and max pooling layer. This saw another dramatic change, this time an increase to an accuracy of **94.0%**.
   `333/333 - 1s - loss: 0.2511 - accuracy: 0.9397 - 1s/epoch - 4ms/step`

5) I tried another convolutional and max pooling layer but this time didn't see a change in accuracy and received an accuracy of **93.5%**. I decided to remove these layers and that 2 convolutional layers and 2 max pooling layers was probably the right amount.
   `333/333 - 1s - loss: 0.2309 - accuracy: 0.9352 - 1s/epoch - 3ms/step`

6) I then decided to experiment with different numbers of hidden layers. I tested each hidden layer **3** times and created an average. I observed a marginal increase with each added layer and decided to have **2 hidden layers** as the increase after 2 was minimal.
   - 1 hidden layer - 94.96%, 93.18%, 94.96%       **Average - 94.37%**
   - 2 hidden layers - 95.77%, 95.52, 95.08%         **Average - 95.46%** 
   - 3 hidden layers - 96.44%, 95.58%, 94.48%      **Average - 95.5%** 
   - 4 hidden layers - 96.02%, 94.28%, 96.43%      **Average - 95.57%**

7) I then experimented with the number of neurons in the hidden layers. After increasing the neurons in each layer to **256**, I experienced an accuracy decrease to approximately **94.1%**. I then decreased the count to **64** and experienced a further decrease to **92.5%** and so I decided that the initial value of **128** was the ideal number.

8) I then increased the pool size to a **3x3** grid and experienced an accuracy decrease to **79.3%**. I decided that as the images provided were relatively small, a larger pool size wouldn't properly isolate outlines and so a **2x2** grid was ideal.

9) Finally, I increased the number of filters to **64** and didn't get an accuracy change but instead experienced a longer training time. After decreasing it to **16** I got an accuracy of **90.7%** and so decided on **32** as the right number of filters.

10) My final model consisted of **2 Convolutional Layers**, **2 Max Pooling Layers** and **2 Hidden Layers** with a dropout of **0.5**. This yielded an approximate accuracy of **95.5%**.
