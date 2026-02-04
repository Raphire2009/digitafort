# Pattern Recognition in Algorithmic Thinking

## Introduction

Pattern recognition is the process of identifying similarities, regularities, or patterns in data. This is a fundamental pillar of computational thinking and algorithmic problem-solving. By recognizing patterns, we can simplify complex problems, make predictions, and develop more efficient solutions.

## Why Pattern Recognition Matters

Pattern recognition helps us:
- **Reduce complexity**: By identifying repeating elements, we can simplify problems
- **Predict outcomes**: Recognized patterns allow us to anticipate what comes next
- **Optimize solutions**: Finding patterns often reveals more efficient algorithms
- **Generalize solutions**: Patterns help us create solutions that work for multiple cases
- **Automate processes**: Recognizing patterns enables us to write code that handles various scenarios

## Types of Patterns

### 1. Sequence Patterns
Patterns that follow a specific order or progression.

```python
# Example: Fibonacci Sequence
def recognize_fibonacci_pattern():
    """
    The Fibonacci sequence: each number is the sum of the two preceding ones
    Pattern: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    """
    sequence = [0, 1]
    
    # Generate next 10 numbers by recognizing the pattern
    for i in range(10):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    print("Fibonacci Sequence:", sequence)
    return sequence

# Example: Arithmetic Progression
def recognize_arithmetic_pattern(data):
    """
    Recognize if a sequence follows an arithmetic pattern
    Example: 2, 5, 8, 11, 14 (difference of 3)
    """
    if len(data) < 2:
        return None
    
    differences = [data[i+1] - data[i] for i in range(len(data)-1)]
    
    # Check if all differences are the same
    if len(set(differences)) == 1:
        common_diff = differences[0]
        print(f"Arithmetic pattern found! Common difference: {common_diff}")
        
        # Predict next 5 numbers
        predictions = []
        last_num = data[-1]
        for i in range(1, 6):
            predictions.append(last_num + (common_diff * i))
        
        print(f"Next 5 numbers will be: {predictions}")
        return common_diff, predictions
    else:
        print("No arithmetic pattern found")
        return None

# Test it
data = [2, 5, 8, 11, 14, 17]
recognize_arithmetic_pattern(data)
```

### 2. Structural Patterns
Patterns in how data is organized or structured.

```python
# Example: Detecting Palindromes
def is_palindrome(text):
    """
    Palindrome pattern: reads the same forwards and backwards
    Examples: 'racecar', 'madam', '12321'
    """
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

# Example: Nested Structures
def analyze_nested_structure(data):
    """
    Recognize patterns in nested data structures
    """
    def count_depth(obj, current_depth=0):
        if isinstance(obj, (list, tuple)):
            if not obj:
                return current_depth
            return max(count_depth(item, current_depth + 1) for item in obj)
        elif isinstance(obj, dict):
            if not obj:
                return current_depth
            return max(count_depth(value, current_depth + 1) for value in obj.values())
        else:
            return current_depth
    
    depth = count_depth(data)
    print(f"Maximum nesting depth: {depth}")
    return depth

# Test nested structure
nested_list = [1, [2, [3, [4, [5]]]]]
analyze_nested_structure(nested_list)
```

### 3. Frequency Patterns
Patterns based on how often elements appear.

```python
from collections import Counter

def analyze_frequency_pattern(data):
    """
    Find the most common elements and their patterns
    """
    freq = Counter(data)
    
    print("Frequency Analysis:")
    for item, count in freq.most_common():
        print(f"  {item}: appears {count} times")
    
    # Find if there's a pattern in frequencies
    frequencies = list(freq.values())
    if len(set(frequencies)) == 1:
        print(f"\nPattern found: All elements appear exactly {frequencies[0]} times (uniform distribution)")
    elif frequencies == sorted(frequencies, reverse=True):
        print("\nPattern found: Zipf's law-like distribution (decreasing frequency)")
    
    return freq

# Example: Text analysis
text = "hello world hello python world hello"
words = text.split()
analyze_frequency_pattern(words)
```

### 4. Repetition Patterns
Identifying cycles and repeating elements.

```python
def find_repeating_pattern(sequence):
    """
    Find if there's a repeating pattern in a sequence
    Example: [1,2,3,1,2,3,1,2,3] has pattern [1,2,3]
    """
    n = len(sequence)
    
    # Try different pattern lengths
    for pattern_length in range(1, n // 2 + 1):
        pattern = sequence[:pattern_length]
        
        # Check if this pattern repeats throughout
        is_repeating = True
        for i in range(pattern_length, n):
            if sequence[i] != pattern[i % pattern_length]:
                is_repeating = False
                break
        
        if is_repeating:
            repetitions = n // pattern_length
            print(f"Repeating pattern found: {pattern}")
            print(f"Pattern repeats {repetitions} times")
            return pattern
    
    print("No repeating pattern found")
    return None

# Test
sequence = [1, 2, 3, 1, 2, 3, 1, 2, 3]
find_repeating_pattern(sequence)
```

## Real-World Applications

### Example 1: Stock Price Pattern Recognition

```python
import random

def generate_stock_data(days=30):
    """Generate simulated stock prices"""
    prices = [100]  # Starting price
    for _ in range(days - 1):
        change = random.uniform(-5, 5)
        prices.append(prices[-1] + change)
    return prices

def detect_trend(prices, window=5):
    """
    Detect upward or downward trends using moving averages
    """
    if len(prices) < window:
        return "Insufficient data"
    
    # Calculate moving averages
    moving_avgs = []
    for i in range(len(prices) - window + 1):
        avg = sum(prices[i:i+window]) / window
        moving_avgs.append(avg)
    
    # Analyze trend
    if len(moving_avgs) < 2:
        return "Neutral"
    
    increases = sum(1 for i in range(1, len(moving_avgs)) 
                   if moving_avgs[i] > moving_avgs[i-1])
    decreases = sum(1 for i in range(1, len(moving_avgs)) 
                   if moving_avgs[i] < moving_avgs[i-1])
    
    if increases > decreases * 1.5:
        return "Strong Upward Trend"
    elif decreases > increases * 1.5:
        return "Strong Downward Trend"
    elif increases > decreases:
        return "Mild Upward Trend"
    elif decreases > increases:
        return "Mild Downward Trend"
    else:
        return "Neutral/Sideways"

# Test
stock_prices = generate_stock_data(30)
trend = detect_trend(stock_prices)
print(f"Stock trend detected: {trend}")
print(f"Prices: {[round(p, 2) for p in stock_prices[:10]]}...")
```

### Example 2: Email Spam Detection Pattern

```python
def detect_spam_patterns(email_text):
    """
    Recognize common spam patterns in email text
    """
    spam_indicators = {
        'urgent_words': ['urgent', 'act now', 'limited time', 'hurry'],
        'money_words': ['free money', 'cash', 'prize', 'winner', '$$$'],
        'suspicious_chars': email_text.count('!') > 3,
        'all_caps_ratio': sum(1 for c in email_text if c.isupper()) / len(email_text) if email_text else 0
    }
    
    score = 0
    reasons = []
    
    # Check for urgent language
    urgent_count = sum(1 for word in spam_indicators['urgent_words'] 
                      if word.lower() in email_text.lower())
    if urgent_count > 0:
        score += urgent_count * 2
        reasons.append(f"Contains {urgent_count} urgent words")
    
    # Check for money-related spam
    money_count = sum(1 for word in spam_indicators['money_words'] 
                     if word.lower() in email_text.lower())
    if money_count > 0:
        score += money_count * 3
        reasons.append(f"Contains {money_count} money-related spam words")
    
    # Check excessive punctuation
    if spam_indicators['suspicious_chars']:
        score += 2
        reasons.append("Excessive exclamation marks")
    
    # Check caps ratio
    if spam_indicators['all_caps_ratio'] > 0.3:
        score += 3
        reasons.append(f"High ratio of capital letters ({spam_indicators['all_caps_ratio']:.1%})")
    
    # Determine result
    if score >= 5:
        result = "SPAM"
    elif score >= 2:
        result = "SUSPICIOUS"
    else:
        result = "LEGITIMATE"
    
    print(f"\nEmail Classification: {result}")
    print(f"Spam Score: {score}")
    if reasons:
        print("Reasons:")
        for reason in reasons:
            print(f"  - {reason}")
    
    return result, score

# Test
email1 = "URGENT!!! You've WON $1,000,000!!! ACT NOW!!! Limited time!!!"
email2 = "Hi, just wanted to follow up on our meeting next week."

print("Email 1:")
detect_spam_patterns(email1)

print("\n" + "="*50)
print("Email 2:")
detect_spam_patterns(email2)
```

### Example 3: Image Pattern Recognition (Simplified)

```python
def detect_image_pattern(grid):
    """
    Detect patterns in a simple grid (representing pixels)
    Useful for basic shape recognition
    """
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    
    # Check for horizontal lines
    horizontal_lines = sum(1 for row in grid if all(cell == 1 for cell in row))
    
    # Check for vertical lines
    vertical_lines = 0
    for col in range(cols):
        if all(grid[row][col] == 1 for row in range(rows)):
            vertical_lines += 1
    
    # Check for diagonal pattern (top-left to bottom-right)
    diagonal = all(grid[i][i] == 1 for i in range(min(rows, cols)))
    
    # Check for symmetry
    horizontal_symmetry = all(grid[i] == grid[rows-1-i] for i in range(rows//2))
    vertical_symmetry = all(
        all(grid[i][j] == grid[i][cols-1-j] for i in range(rows))
        for j in range(cols//2)
    )
    
    print("Pattern Analysis:")
    print(f"  Horizontal lines: {horizontal_lines}")
    print(f"  Vertical lines: {vertical_lines}")
    print(f"  Diagonal pattern: {diagonal}")
    print(f"  Horizontal symmetry: {horizontal_symmetry}")
    print(f"  Vertical symmetry: {vertical_symmetry}")
    
    # Visualize the grid
    print("\nGrid visualization:")
    for row in grid:
        print("  " + "".join("█" if cell == 1 else "·" for cell in row))

# Test with a simple pattern (cross shape)
cross_pattern = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

detect_image_pattern(cross_pattern)
```

## Advanced Pattern Recognition Techniques

### Using Regular Expressions

```python
import re

def extract_patterns_with_regex(text):
    """
    Use regex to find common patterns in text
    """
    patterns = {
        'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phones': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'urls': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        'dates': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
        'prices': r'\$\d+(?:\.\d{2})?'
    }
    
    results = {}
    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            results[pattern_name] = matches
            print(f"{pattern_name.capitalize()} found: {matches}")
    
    return results

# Test
sample_text = """
Contact us at support@company.com or call 555-123-4567.
Visit our website at https://www.example.com
Special offer: $29.99 until 12/25/2024!
Alternative contact: info@example.org or 555.987.6543
"""

extract_patterns_with_regex(sample_text)
```

### Machine Learning Pattern Recognition (Conceptual)

```python
def simple_classifier(features, training_data):
    """
    A simplified example of how ML recognizes patterns
    Using k-nearest neighbors concept
    """
    def distance(point1, point2):
        """Calculate Euclidean distance"""
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5
    
    # Find closest training examples
    distances = []
    for data_point, label in training_data:
        dist = distance(features, data_point)
        distances.append((dist, label))
    
    # Sort by distance and get 3 nearest neighbors
    distances.sort()
    nearest = distances[:3]
    
    # Vote for most common label
    labels = [label for _, label in nearest]
    prediction = max(set(labels), key=labels.count)
    
    print(f"Input features: {features}")
    print(f"Nearest neighbors: {nearest}")
    print(f"Predicted class: {prediction}")
    
    return prediction

# Example: Classify fruits based on [weight, sweetness]
training_data = [
    ([150, 8], 'apple'),
    ([160, 7], 'apple'),
    ([140, 9], 'apple'),
    ([200, 5], 'orange'),
    ([210, 4], 'orange'),
    ([190, 6], 'orange'),
    ([300, 9], 'banana'),
    ([310, 10], 'banana'),
    ([290, 8], 'banana'),
]

# Classify a new fruit
new_fruit = [155, 8]
simple_classifier(new_fruit, training_data)
```

## Practice Exercises

### Exercise 1: Temperature Pattern Analyzer

```python
def analyze_temperature_pattern(temperatures):
    """
    Analyze temperature data to find patterns
    - Daily variations
    - Weekly trends
    - Seasonal changes
    """
    # Calculate daily average change
    daily_changes = [temperatures[i+1] - temperatures[i] 
                    for i in range(len(temperatures)-1)]
    avg_change = sum(daily_changes) / len(daily_changes)
    
    # Find cycles (weekly pattern for 7-day data)
    if len(temperatures) >= 7:
        weekly_pattern = temperatures[:7]
        print(f"Weekly pattern: {weekly_pattern}")
    
    # Detect anomalies (temperatures significantly different from average)
    avg_temp = sum(temperatures) / len(temperatures)
    std_dev = (sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)) ** 0.5
    
    anomalies = [temp for temp in temperatures 
                if abs(temp - avg_temp) > 2 * std_dev]
    
    print(f"Average temperature: {avg_temp:.2f}°F")
    print(f"Average daily change: {avg_change:+.2f}°F")
    print(f"Standard deviation: {std_dev:.2f}°F")
    if anomalies:
        print(f"Anomalies detected: {anomalies}")
    
    return avg_temp, avg_change, anomalies

# Test with sample data
temps = [72, 75, 73, 70, 68, 71, 74, 76, 78, 75, 73, 95, 72, 74]
analyze_temperature_pattern(temps)
```

### Exercise 2: User Behavior Pattern

```python
def analyze_user_behavior(login_times):
    """
    Analyze when users typically log in
    Input: list of hour values (0-23)
    """
    from collections import Counter
    
    hour_frequency = Counter(login_times)
    
    # Find peak hours
    peak_hour = hour_frequency.most_common(1)[0]
    
    # Categorize by time of day
    time_categories = {
        'morning': sum(hour_frequency[h] for h in range(6, 12)),
        'afternoon': sum(hour_frequency[h] for h in range(12, 18)),
        'evening': sum(hour_frequency[h] for h in range(18, 24)),
        'night': sum(hour_frequency[h] for h in range(0, 6))
    }
    
    total_logins = len(login_times)
    
    print("User Login Pattern Analysis:")
    print(f"Total logins: {total_logins}")
    print(f"Peak hour: {peak_hour[0]}:00 ({peak_hour[1]} logins)")
    print("\nLogin distribution:")
    for period, count in time_categories.items():
        percentage = (count / total_logins) * 100
        print(f"  {period.capitalize()}: {count} ({percentage:.1f}%)")
    
    return hour_frequency, time_categories

# Test
login_hours = [9, 10, 9, 14, 15, 9, 10, 20, 21, 9, 10, 11, 14, 15, 16, 20, 21, 22]
analyze_user_behavior(login_hours)
```

## Key Takeaways

1. **Pattern recognition is everywhere**: From data analysis to algorithm optimization, recognizing patterns is fundamental to problem-solving.

2. **Start simple**: Look for basic patterns first (repetition, sequences, frequency) before moving to complex ones.

3. **Use the right tools**: Regular expressions for text, statistical methods for numerical data, and appropriate data structures for organizing information.

4. **Patterns enable prediction**: Once you identify a pattern, you can make informed predictions about future data or behavior.

5. **Combine multiple techniques**: Real-world problems often require recognizing multiple types of patterns simultaneously.

6. **Practice regularly**: The more you practice recognizing patterns, the better you become at identifying them quickly and accurately.

## Further Learning

To deepen your pattern recognition skills:
- Study time series analysis
- Learn about machine learning algorithms
- Explore data visualization techniques
- Practice with real-world datasets
- Study algorithm design patterns
- Learn about image and signal processing

Remember: Pattern recognition is not just about finding what's there—it's about understanding why it's there and how you can use that knowledge to solve problems more effectively.