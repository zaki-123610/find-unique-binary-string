def find_different_binary_string(nums: list[str]) -> str:
    return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))


if __name__ == "__main__":
    examples = [
        ["01", "10"],
        ["00", "01"],
        ["111", "011", "001"],
        ["0"],
    ]

    for nums in examples:
        result = find_different_binary_string(nums)
        assert len(result) == len(nums)
        assert result not in nums
        print(f"{nums} -> {result}")

    print("All tests passed.")
