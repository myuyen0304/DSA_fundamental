#!/usr/bin/env python3
"""
DSA Learning - Demo Script
Run this to see all examples in action!
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def demo_complexity_analysis():
    """Demo complexity analysis examples"""
    print_section("COMPLEXITY ANALYSIS EXAMPLES")
    
    try:
        from complexity_analysis import examples
        
        print("Running complexity comparison demo...")
        print("This will show you the performance difference between")
        print("O(1), O(log n), O(n), O(n²), and O(2ⁿ)\n")
        
        examples.demo_comparison()
        examples.demo_fibonacci_comparison()
        
    except Exception as e:
        print(f"Error running complexity examples: {e}")
        print("Make sure you're in the 01_fundamentals directory")


def demo_arrays():
    """Demo array implementations"""
    print_section("ARRAY TECHNIQUES EXAMPLES")
    
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        from arrays import implementation
        
        print("1. TWO POINTERS")
        arr = [1, 2, 3, 4, 6]
        target = 6
        print(f"   Array: {arr}")
        print(f"   Target sum: {target}")
        result = implementation.two_sum_sorted(arr, target)
        print(f"   Indices with sum={target}: {result}")
        print(f"   Values: [{arr[result[0]]}, {arr[result[1]]}]")
        
        print("\n2. SLIDING WINDOW")
        arr = [2, 1, 5, 1, 3, 2]
        k = 3
        print(f"   Array: {arr}")
        print(f"   Window size: {k}")
        result = implementation.max_sum_subarray_fixed(arr, k)
        print(f"   Maximum sum of any subarray of size {k}: {result}")
        
        print("\n3. KADANE'S ALGORITHM")
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        print(f"   Array: {arr}")
        result = implementation.max_subarray_sum(arr)
        print(f"   Maximum subarray sum: {result}")
        
        print("\n4. DUTCH NATIONAL FLAG")
        arr = [2, 0, 2, 1, 1, 0]
        print(f"   Before: {arr}")
        implementation.sort_colors(arr)
        print(f"   After:  {arr}")
        
        print("\n5. BINARY SEARCH")
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 13
        print(f"   Sorted array: {arr}")
        print(f"   Target: {target}")
        result = implementation.binary_search(arr, target)
        print(f"   Found at index: {result}")
        
    except Exception as e:
        print(f"Error running array examples: {e}")
        print("Make sure you're in the 02_linear_structures directory")


def show_complexity_table():
    """Show Big O complexity comparison"""
    print_section("BIG O COMPLEXITY COMPARISON")
    
    print("Input Size n = 1,000,000 (1 million)")
    print("-" * 70)
    print(f"{'Complexity':<15} {'Operations':<20} {'Approx Time':<15} {'Rating'}")
    print("-" * 70)
    
    data = [
        ("O(1)", "1", "Instant", "⭐⭐⭐⭐⭐"),
        ("O(log n)", "~20", "Instant", "⭐⭐⭐⭐⭐"),
        ("O(n)", "1,000,000", "1 ms", "⭐⭐⭐⭐"),
        ("O(n log n)", "~20,000,000", "20 ms", "⭐⭐⭐"),
        ("O(n²)", "1,000,000,000,000", "17 minutes", "⭐"),
        ("O(2ⁿ)", "2^n", "Universe age", "❌"),
    ]
    
    for complexity, ops, time, rating in data:
        print(f"{complexity:<15} {ops:<20} {time:<15} {rating}")
    
    print("-" * 70)
    print("\nKey Insight: Complexity matters A LOT as input size grows!")


def show_patterns_summary():
    """Show common patterns summary"""
    print_section("COMMON DSA PATTERNS")
    
    patterns = [
        ("Two Pointers", "O(n)", "Sorted array, pairs, palindrome"),
        ("Sliding Window", "O(n)", "Subarray/substring problems"),
        ("Binary Search", "O(log n)", "Sorted array search"),
        ("Hash Map", "O(n)", "Fast lookup, count frequency"),
        ("Prefix Sum", "O(1) query", "Range sum queries"),
        ("DFS/BFS", "O(V+E)", "Tree/graph traversal"),
        ("Dynamic Programming", "Varies", "Optimization problems"),
        ("Backtracking", "O(2ⁿ)", "Generate combinations"),
    ]
    
    print(f"{'Pattern':<25} {'Complexity':<15} {'Use Case'}")
    print("-" * 70)
    
    for pattern, complexity, use_case in patterns:
        print(f"{pattern:<25} {complexity:<15} {use_case}")
    
    print("-" * 70)
    print("\nMaster these patterns and you can solve most problems!")


def main():
    """Main demo function"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "DSA LEARNING - DEMO SCRIPT" + " "*27 + "║")
    print("║" + " "*11 + "Welcome to Your DSA Learning Journey!" + " "*20 + "║")
    print("╚" + "="*68 + "╝")
    
    print("\nThis script demonstrates the concepts you'll learn.")
    print("Choose what you want to see:\n")
    
    print("1. Complexity Analysis (with timing)")
    print("2. Array Techniques")
    print("3. Complexity Comparison Table")
    print("4. Common Patterns Summary")
    print("5. All of the above")
    print("0. Exit")
    
    while True:
        try:
            choice = input("\nYour choice (0-5): ").strip()
            
            if choice == "0":
                print("\nHappy learning! 🚀")
                break
            elif choice == "1":
                demo_complexity_analysis()
            elif choice == "2":
                demo_arrays()
            elif choice == "3":
                show_complexity_table()
            elif choice == "4":
                show_patterns_summary()
            elif choice == "5":
                show_complexity_table()
                show_patterns_summary()
                demo_arrays()
                print("\n(Skipping complexity timing demos - run option 1 separately)")
            else:
                print("Invalid choice. Please enter 0-5.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nExiting... Happy learning! 🚀")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Make sure you're in the correct directory!")
            break


if __name__ == "__main__":
    main()
