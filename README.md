# 💻 LEETCODE — Algorithm Solutions & Practice

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/shreyas026/LEETCODE/actions/workflows/ci.yml/badge.svg)](https://github.com/shreyas026/LEETCODE/actions)
[![Stars](https://img.shields.io/github/stars/shreyas026/LEETCODE?style=social)](https://github.com/shreyas026/LEETCODE/stargazers)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![LeetCode](https://img.shields.io/badge/LeetCode-200%2B_solutions-orange.svg)](https://leetcode.com)

**Curated collection of 200+ LeetCode solutions with detailed explanations, multiple approaches, and complexity analysis. Auto-updated with daily practice tracking.**

---

## 🎯 Features

- ✅ **200+ Solutions** — Covering Easy, Medium, Hard problems
- 📝 **Detailed Explanations** — Approach, intuition, step-by-step walkthrough
- ⚡ **Multiple Approaches** — Brute force → Optimized → Optimal
- 📊 **Complexity Analysis** — Time & Space for each solution
- 🏷️ **Categorized** — By topic, difficulty, pattern
- 🔄 **Auto-Update** — Daily sync with LeetCode submissions
- 🧪 **Test Cases** — Comprehensive test suites for each problem
- 📈 **Progress Tracking** — Stats dashboard, streak counter

---

## 📁 Structure

`
LEETCODE/
├── solutions/
│   ├── easy/              # Easy problems
│   ├── medium/            # Medium problems
│   └── hard/              # Hard problems
├── patterns/              # By algorithmic pattern
│   ├── two-pointers/
│   ├── sliding-window/
│   ├── binary-search/
│   ├── dfs-bfs/
│   ├── dynamic-programming/
│   ├── backtracking/
│   ├── greedy/
│   ├── heap/
│   ├── trie/
│   └── graph/
├── topics/                # By topic
│   ├── arrays/
│   ├── strings/
│   ├── linked-lists/
│   ├── trees/
│   ├── graphs/
│   └── dp/
├── tests/                 # Unit tests
├── scripts/               # Auto-update scripts
├── stats/                 # Progress tracking
├── requirements.txt
└── README.md
`

---

## 📊 Progress Stats

| Difficulty | Solved | Total | Progress |
|------------|--------|-------|----------|
| Easy       | 80+    | ~700  | ~11%     |
| Medium     | 100+   | ~1500 | ~7%      |
| Hard       | 20+    | ~600  | ~3%      |
| **Total**  | **200+** | **~2800** | **~7%**  |

| Pattern | Problems |
|---------|----------|
| Two Pointers | 25 |
| Sliding Window | 18 |
| Binary Search | 22 |
| DFS/BFS | 30 |
| Dynamic Programming | 35 |
| Backtracking | 15 |
| Greedy | 12 |
| Heap/Priority Queue | 10 |
| Trie | 8 |
| Graph Algorithms | 20 |

---

## ⚙️ Quick Start

### 1. Clone & Install
`ash
git clone https://github.com/shreyas026/LEETCODE.git
cd LEETCODE
pip install -r requirements.txt
`

### 2. Run Tests
`ash
# All tests
pytest tests/ -v

# Specific problem
pytest tests/solutions/medium/test_two_sum.py -v

# With coverage
pytest --cov=solutions --cov-report=html
`

### 3. View Solutions
`ash
# List all problems
python scripts/list_problems.py

# View specific solution
cat solutions/medium/two_sum.py
`

---

## 🔄 Auto-Update System

The repository auto-syncs with LeetCode submissions via GitHub Actions:

- **Daily Cron** — Runs every day at 6 AM UTC
- **Fetches** new submissions from LeetCode API
- **Formats** code with explanations
- **Updates** stats and progress tracking
- **Commits** changes automatically

### Setup Auto-Update
1. Add LEETCODE_SESSION and LEETCODE_CSRF_TOKEN as GitHub Secrets
2. Enable workflow in Actions tab
3. Runs daily automatically

---

## 📚 Problem Format

Each solution includes:
`python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array, Hash Table

Approach 1: Brute Force - O(n²) time, O(1) space
Approach 2: Hash Map - O(n) time, O(n) space ⭐ Optimal
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map approach
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Test cases
if __name__ == '__main__':
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0,1]
    assert sol.twoSum([3,2,4], 6) == [1,2]
    print('All tests passed!')
`

---

## 🏷️ Topics Covered

- **Arrays & Strings** — Two pointers, sliding window, prefix sums
- **Linked Lists** — Fast/slow pointers, reversal, cycle detection
- **Trees & Graphs** — DFS, BFS, topological sort, MST
- **Dynamic Programming** — 1D/2D DP, bitmask, interval DP
- **Backtracking** — Permutations, combinations, subsets, N-Queens
- **Greedy** — Interval scheduling, Huffman, MST
- **Heaps** — Top K, median finder, task scheduler
- **Tries** — Prefix search, autocomplete, XOR problems
- **Bit Manipulation** — XOR tricks, bit counting, masks
- **Math & Geometry** — GCD, modular arithmetic, convex hull

---

## 🧪 Testing

`ash
# Run all tests
pytest

# Run with coverage
pytest --cov=solutions --cov-report=term-missing

# Run specific pattern
pytest tests/patterns/two_pointers/ -v

# Run specific topic
pytest tests/topics/arrays/ -v
`

---

## 📈 Contributing

1. Add new solutions in solutions/<difficulty>/
2. Follow the standard format (docstring + class + tests)
3. Add tests in 	ests/
4. Run pytest to verify
5. Submit PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License
MIT License — see [LICENSE](LICENSE)

---

## 🔗 Links
- **LeetCode Profile**: https://leetcode.com/shreyas026/
- **Repository**: https://github.com/shreyas026/LEETCODE
