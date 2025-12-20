import random
import numpy as np

class RandomAgent:
    def __init__(self, n_actions=4):
        self.n_actions = n_actions
        self.episodeStepLimit = 10
        self.minSteps = 10**6
        

    def choose_action(self, state, greedy=False):
        
        # 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT
        return random.randint(0, self.n_actions - 1)

    def update(self, s, a, r, s_next):
        
        pass

    def run(self, env):
        
        for episode in range(self.episodeStepLimit):
            noSteps = 0
            s = env.reset()
            done = False
            
            
            for steps in range(100):
                
                action = self.choose_action(s)
                
                # 2. Apply move to the grid
                s_next, reward, done = env.step(action)
                noSteps += 1
                s = s_next
                
                # 3. Visuals
                env.render(delay=0.05)
                
                if done:
                    print(f"Goal Reached in {noSteps} steps!")
                    if noSteps <= self.minSteps:
                        print(f"The episode with the shortest number of steps so far is {episode}")
                        print(f"The smallest number of steps so far is {noSteps}")
                        self.minSteps = noSteps
                    break
            
            if not done:
                print(f"Episode {episode} failed to reach goal within 100 steps.")
