def solution(data, ext, val_ext, sort_by):
  categories = ["code", "date", "maximum", "remain"]
  idx = categories.index(ext)
  sort_idx = categories.index(sort_by)
  res = sorted([d for d in data if d[idx] < val_ext], key = lambda x : x[sort_idx])

  return res

# 간단한 구현문제 (프로그래머스 Lv1.)