
from typing import Callable

def calculate_score(trigger_tokens: list[str], given_tokens: list[str]) -> float:
    score: int = 0
    
    for token in given_tokens:
        if token in trigger_tokens:
            score += 1
    
    # Return as a precentage
    return score / len(trigger_tokens) * 100
            

def probability_test(given_tokens: list, func_token_map: dict[Callable[[None], str], list[str]]) -> dict[Callable, float]:
    score_map: dict[Callable, float] = dict()
    
    for func, tokens in func_token_map.items():
        score_map[func] = calculate_score(tokens, given_tokens)
        
    return score_map

def get_time() -> None:
    pass
def web_search() -> None:
    pass
def code() -> None:
    pass

test_tokens = ["search", "web", "python"] 
test_map = {
    get_time: ["time", "clock"],
    web_search: ["search", "web"],
    code: ["python", "program", "code"]
}

score_map = probability_test(test_tokens, test_map)
# Sort by score (value) descending and keep function reference with score
sorted_score_map = sorted(score_map.items(), key=lambda kv: kv[1], reverse=True)
# Print function names with their scores
for func, score in sorted_score_map:
    print(f"{func.__name__}: {score}")