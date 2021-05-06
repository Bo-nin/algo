def fun(n, tpList, phaseV):
  # print(phaseV)
  if phaseV[0] == n:
    return phaseV[2]
  if (phaseV[1] > 0 or tpList[phaseV[0]][0] > n-phaseV[0]) :
    return fun(n, tpList, [phaseV[0]+1,phaseV[1]-1,phaseV[2]])

  tryPhaseV = fun(n, tpList, [phaseV[0]+1,tpList[phaseV[0]][0]-1,phaseV[2]+tpList[phaseV[0]][1]])
  nonPhaseV = fun(n, tpList, [phaseV[0]+1,phaseV[1],phaseV[2]])
  return(max([tryPhaseV,nonPhaseV]))

n = int(input())
tpList = [list(map(int, input().split())) for _ in range(n)]
print(fun(n, tpList, [0,0,0]))