memoryTable = {
  "BOOL": 1,
  "SHORT": 2,
  "FLOAT": 4,
  "INT": 8,
  "LONG": 16,
}

def solution(S):
  answer = []
  nowMemory = []
  for s in S:
    if memoryTable[s] == 16:
      for _ in range(8-len(nowMemory)):
        nowMemory.append(".")
      answer.append(''.join(nowMemory))
      answer.append('########')
      answer.append('########')
      nowMemory = []
      continue
    if memoryTable[s] > 8-len(nowMemory):
      for _ in range(8-len(nowMemory)):
        nowMemory.append(".")
      answer.append(''.join(nowMemory))
      nowMemory = []
      for _ in range(memoryTable[s]):
        nowMemory.append("#")
    else:
      blink = (8-len(nowMemory)) % memoryTable[s]
      for _ in range(blink):
        nowMemory.append(".")
      for _ in range(memoryTable[s]):
        nowMemory.append("#")
  if len(nowMemory) > 0:
    for _ in range(8-len(nowMemory)):
      nowMemory.append(".")
    answer.append(''.join(nowMemory))
  
  if len(answer) > 16:
    return 'HALT'
  else:
    return ','.join(answer)
print(solution(["INT","SHORT","FLOAT","INT","BOOL"]))