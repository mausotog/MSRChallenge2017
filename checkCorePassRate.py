import sys

with open('./confoundAndSocData.csv','r') as fin:
    coreTeamMemberCount = 0
    coreAndPassedCount = 0
    nonCoreTeamMemberCount = 0
    nonCoreAndPassedCount = 0
    for lineCount,line in enumerate(fin):
        if lineCount == 0:
            continue
        line = line.rstrip()
        lineItems = line.split(',')
        if lineItems[10] == 'TRUE':
            coreTeamMemberCount += 1
            if lineItems[-1] == '"passed"':
                coreAndPassedCount += 1
        elif lineItems[10] == 'FALSE':
            nonCoreTeamMemberCount += 1
            if lineItems[-1] == '"passed"':
                nonCoreAndPassedCount += 1
        else:
            print(line)
            sys.exit(1)
print('core team member success rate: {0:.2%} ({1}/{2})'.format(coreAndPassedCount/coreTeamMemberCount,coreAndPassedCount, coreTeamMemberCount))
print('non core team member success rate: {0:.2%} ({1}/{2})'.format(nonCoreAndPassedCount/nonCoreTeamMemberCount,nonCoreAndPassedCount,nonCoreTeamMemberCount))
print('non core team member percentage: {0:.2%} ({1}/{2})'.format(nonCoreTeamMemberCount/(nonCoreTeamMemberCount + coreTeamMemberCount),nonCoreTeamMemberCount, (nonCoreTeamMemberCount+coreTeamMemberCount)))

print('core team member percentage: {0:.2%} ({1}/{2})'.format(coreTeamMemberCount/(nonCoreTeamMemberCount + coreTeamMemberCount),coreTeamMemberCount, (nonCoreTeamMemberCount+coreTeamMemberCount)))
#print('nonCoreTeamMemberCount: {0}'.format(nonCoreTeamMemberCount))
#print('nonCoreAndPassedCount: {0}'.format(nonCoreAndPassedCount))


