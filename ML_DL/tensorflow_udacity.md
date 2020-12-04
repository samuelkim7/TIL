### Concept
- Just give pairs of input and output and let the computer figure out the best algorithm. And this learning process is done by tuning the variables of the equation.
```python
l0 = tf.keras.layers.Dense(units=1, input_shape=[1]) 
model = tf.keras.Sequential([l0])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
model.predict([100.0])
```
- This example is the general plan for of any machine learning program. You will use the same structure to create and train your neural network, and use it to make predictions.
- Training Process: The training process (happening in model.fit(...)) is really about tuning the internal variables of the networks to the best possible values, so that they can map the input to the output. This is achieved through an optimization process called Gradient Descent.
