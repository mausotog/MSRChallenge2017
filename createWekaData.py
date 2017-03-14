import re
import collections

def subFunction(m):
    if m.group(1):
        return ';'
    else:
        return m.group(0)

def createCountDict():
    return collections.defaultdict(int)

projectDict = collections.defaultdict(createCountDict)
#statusDict = collections.defaultdict(int)
locationDict = collections.defaultdict(int)
csvPattern = re.compile('".*,.*"|(,)')
with open('augmentedDataSetSAMPLE.csv','r') as fin:
    for line in fin:
        newLine = re.sub(csvPattern, subFunction, line)
        print(newLine)
        lineItems = newLine.split(';')
        projectDict[lineItems[0]][lineItems[2]] += 1
        locationDict[lineItems[7]] += 1

print('')
for project, statusDict in projectDict.items():
    total = 0
    passedCount = 0
    for status, count in statusDict.items():
        total += count
        if status == 'passed':
            passedCount= count
    print('percent of non-passing projects: {0:%}'.format((total - passedCount)/total))
#print(projectDict)
print('')
print(statusDict)
print('')
print(locationDict)

with open('wekaData.arff','w') as outFile:
    print('% weka data for the MSR mining challenge 2017',file=outFile)
    print('',file=outFile)
    print('@RELATION commitBuild',file=outFile)
    print('',file=outFile)
    projects = ''
    for project in projectDict.keys():
        if projects == '':
            projects = project
        else:
            projects = projects + ',{0}'.format(project)
    print('@ATTRIBUTE projectName {{{0}}}'.format(projects),file = outFile)
    print('@ATTRIBUTE ownedRespositories NUMERIC', file = outFile)
    print('@ATTRIBUTE stars NUMERIC',file = outFile)
    print('@ATTRIBUTE followers NUMERIC', file = outFile)
    print('@ATTRIBUTE following NUMERIC', file = outFile)
    locations = ''
    for location in locationDict.keys():
        location = location.replace(',','-')
        location = location.replace(' ','-')
        location = location.replace('"','')
        location = location.replace("'",'')
        if locations == '':
            locations = location
        else:
            locations = locations + ',{0}'.format(location)
    print('@ATTRIBUTE location {{{0}}}'.format(locations),file = outFile)
    print('@ATTRIBUTE projectsCollaboratedLastYear NUMERIC', file = outFile)
    print('@ATTRIBUTE status {passed,failed,errored}',file = outFile)
    print('',file= outFile)
    print('@DATA', file= outFile)
    with open('augmentedDataSetSAMPLE.csv','r') as fin:
        for line in fin:
            newLine = re.sub(csvPattern, subFunction, line)
            lineItems = newLine.split(';')
            location = lineItems[7]
            location = location.replace(',','-')
            location = location.replace(' ','-')
            location = location.replace('"','')
            location = location.replace("'",'')
            projectsLastYear = lineItems[8].rstrip()
            if projectsLastYear == '':
                print(line)
                projectsLastYear = '?'
            print('{0},{1},{2},{3},{4},{5},{6},{7}'.format(lineItems[0], lineItems[3], lineItems[4], lineItems[5], lineItems[6], location, projectsLastYear, lineItems[2]), file= outFile)




