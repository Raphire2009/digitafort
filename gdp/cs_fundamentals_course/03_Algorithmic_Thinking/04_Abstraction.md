# Abstraction

Abstraction is the process of hiding complex implementation details and showing only the essential features of the object. It's about simplifying a complex reality by modeling classes appropriate to the problem. This is a key step in algorithmic thinking, as it allows you to create a more general-purpose algorithm and focus on the bigger picture.

When you're abstracting a problem, you identify the essential features and ignore the irrelevant ones. You create a simplified model of the problem that captures the necessary characteristics.

## Practical Example: Driving a Car

A perfect real-world example of abstraction is driving a car.

To drive a car, you don't need to know how the engine works, how the transmission system shifts gears, or how the fuel injection system operates. The car's designers have hidden these complex details.

Instead, you interact with a simplified interface:
- **Steering wheel:** to turn.
- **Accelerator pedal:** to go faster.
- **Brake pedal:** to slow down.

This abstraction allows you to use the car for its main purpose—transportation—without being an expert mechanic. You focus on the "what" (driving) rather than the "how" (the internal mechanics).

## Python Program Example: A Car Class

In programming, we use abstraction to manage complexity. We create classes and objects that expose a simple interface to the user, while hiding the complex logic inside.

Here is a Python example that models the car analogy. The `Car` class is an abstraction. The driver (the person using the `Car` object) only needs to know about `start()`, `accelerate()`, and `brake()`. They don't need to know about the `_check_fuel()`, `_ignite_spark_plug()`, or `_inject_fuel()` methods, which are hidden implementation details.

```python
import time

class Car:
    """
    Represents a car. The internal mechanics are abstracted away from the driver.
    The methods starting with an underscore (_) are internal implementation details
    that the driver does not need to know about.
    """
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._is_running = False
        self._speed = 0
        self._fuel_level = 100.0

    # --- Internal (hidden) methods ---
    def _check_fuel(self):
        """Internal method to check if there is fuel."""
        print("   - (Internal) Checking fuel...")
        if self._fuel_level > 0:
            return True
        else:
            print("   - (Internal) Out of fuel!")
            return False

    def _ignite_spark_plug(self):
        """Internal method simulating spark plug ignition."""
        print("   - (Internal) Spark plug fires.")
        time.sleep(0.5)

    def _inject_fuel(self):
        """Internal method simulating fuel injection."""
        print("   - (Internal) Injecting fuel into engine.")
        self._fuel_level -= 2.5 # Consume some fuel to start
        time.sleep(0.5)

    # --- Public (exposed) interface for the driver ---
    def start(self):
        """
        Starts the car. This is part of the public interface.
        It calls several complex, hidden methods.
        """
        print("\nTurning the key to start the car...")
        if not self._is_running and self._check_fuel():
            self._inject_fuel()
            self._ignite_spark_plug()
            self._is_running = True
            print(f"The {self.make} {self.model}'s engine is now running!")
        elif self._is_running:
            print("The car is already running.")
        else:
            print("Cannot start the car.")

    def accelerate(self):
        """Makes the car go faster."""
        if self._is_running and self._fuel_level > 0:
            self._fuel_level -= 5
            self._speed += 10
            print(f"\nAccelerating... Current speed: {self._speed} mph.")
            if self._fuel_level <= 0:
                print("Warning: Ran out of fuel!")
                self._is_running = False
                self._speed = 0
        else:
            print("\nCannot accelerate. The engine is not running.")
            
    def brake(self):
        """Slows the car down."""
        if self._speed > 0:
            self._speed -= 15
            if self._speed < 0:
                self._speed = 0
            print(f"\nBraking... Current speed: {self._speed} mph.")
        else:
            print("\nThe car is already stopped.")

    def get_status(self):
        """Reports the current status of the car."""
        status = "running" if self._is_running else "off"
        print(f"\n--- Car Status ---")
        print(f"  Speed: {self._speed} mph")
        print(f"  Engine: {status}")
        print(f"  Fuel: {self._fuel_level:.2f}%")
        print(f"--------------------")


# --- Using the Abstraction ---
# The driver only needs to know these simple commands.
if __name__ == "__main__":
    my_car = Car("Tesla", "Model S") # Oops, let's pretend it's a gas car for the example :)
    
    # The driver interacts with the simple, abstract interface.
    my_car.get_status()
    my_car.start()
    my_car.get_status()
    my_car.accelerate()
    my_car.accelerate()
    my_car.get_status()
    my_car.brake()
    my_car.get_status()
```

### Benefits of Abstraction in this Code:

*   **Simplicity:** The person using the `Car` object doesn't need to understand the complex sequence of events required to start an engine. They just call `my_car.start()`.
*   **Maintainability:** If we want to change how the engine works (e.g., make it more fuel-efficient by changing the `_inject_fuel` logic), we can do so without changing the way the driver interacts with the car. The public methods (`start`, `accelerate`) remain the same.
*   **Reduces Complexity:** It hides the unnecessary details from the user, allowing them to focus on their goal (driving the car).
