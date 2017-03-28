import sys
with open('./confoundAndSocData.csv','r') as fin:
    followerZeroCount = 0
    followerZeroPassCount = 0
    largeFollowers = 0
    multipleFollowers = 0
    multipleFollowersPassCount = 0
    largeFollowersPassCount = 0
    for lineCount,line in enumerate(fin):
        if lineCount != 0:
            line = line.rstrip()
            lineItems = line.split(',')
            followers = lineItems[-4]
            if followers == '?' or followers == '':
                continue
            elif followers == '0':
                followerZeroCount += 1
                if lineItems[-1] == '"passed"':
                    followerZeroPassCount += 1
            else:
                followerCount = int(followers)
                if followerCount > 1000:
                    largeFollowers += 1
                    if lineItems[-1] == '"passed"':
                        largeFollowersPassCount += 1
                multipleFollowers += 1
                if lineItems[-1] == '"passed"':
                    multipleFollowersPassCount += 1
print('zero followers pass rate : {0:.2%} ({1}/{2})'.format(followerZeroPassCount/(followerZeroCount),followerZeroPassCount,followerZeroCount))
print('multipleFollowers pass rate : {0:.2%} ({1}/{2})'.format(multipleFollowersPassCount/ multipleFollowers, multipleFollowersPassCount, multipleFollowers))
print('largeFollowers pass rate: {0:.2%} ({1}/{2})'.format(largeFollowersPassCount/ largeFollowers, largeFollowersPassCount,largeFollowers))
print('zero followers total: {0:.2%} ({1}/{2})'.format(followerZeroCount/(followerZeroCount + multipleFollowers),followerZeroCount,followerZeroCount+multipleFollowers))
print('multiple followers: {0:.2%} ({1}/{2})'.format(multipleFollowers/(followerZeroCount + multipleFollowers),multipleFollowers,followerZeroCount+multipleFollowers))
print('largeFollowers: {0:.2%} ({1}/{2})'.format(largeFollowers/(followerZeroCount + multipleFollowers),largeFollowers,followerZeroCount+multipleFollowers))


