class Solution:
    # define start_time
    # create prefix sum
    # compare the prev result vs prefix + start_time
    # take the biggest gap and set it as start_time
    def minTime(self, skills: List[int], manas: List[int]) -> int:
        start_time = 0
        prefix_sums = self.get_prefix_sums(skills)
        print(prefix_sums)
        for i, mana in enumerate(manas):
            prev_start_time = start_time
            start_time += manas[i-1] * skills[0] if i != 0 else 0 
            max_delay = 0
            for j, prefix_sum in enumerate(prefix_sums):
                prev_task_finish_time = prev_start_time + prefix_sum * (manas[i-1] if i!= 0 else 0)
                prev_wizard_estimate_finish_time = start_time + (prefix_sums[j-1] * manas[i] if j != 0 else 0)
                delay = prev_task_finish_time - prev_wizard_estimate_finish_time
                # print("Previous task finshed at:                   ", prev_task_finish_time)
                # print("Previous wizard will finish current task at:", prev_wizard_estimate_finish_time)
                max_delay = max(max_delay, delay)
            start_time += max_delay
            #print("-----------------------------------------------")
            #print(start_time)
        return start_time + manas[-1] * prefix_sums[-1]

    def get_prefix_sums(self, skills):
        prefix_sums = []
        for skill in skills:
            if len(prefix_sums) == 0:
                prefix_sums.append(skill)
            else:
                prefix_sums.append(skill + prefix_sums[-1])
        return prefix_sums
            



            