import numpy as np  
import pygame
import time
import new_grid
import matplotlib.pyplot as plt
class QLearningAgent:
    def __init__(self, n_states, n_actions=4, alpha=0.5, gamma=0.99, epsilon=0.2):
        self.Q = np.zeros((n_states, n_actions), dtype=float)
        self.alpha, self.gamma, self.epsilon = alpha, gamma, epsilon
        self.average_rewards = []

    def choose_action(self, state, greedy=False):
        if (not greedy) and (np.random.rand() < self.epsilon):
            return np.random.randint(4)
        return int(np.argmax(self.Q[state]))

    def update(self, s, a, r, s_next):
        
        best_next = np.max(self.Q[s_next])
        td = r + self.gamma * best_next - self.Q[s, a]
        self.Q[s, a] += self.alpha * td

    def plot_reward_curves(self):
        plt.plot(self.average_rewards)
        plt.xlabel("Episode")
        plt.ylabel("Cumulative Reward")
        plt.show()


    def train(self,env,visual_render, episodes=500):
        for ep in range(episodes):
          total_r, steps = 0, 0
          s = env.reset()
          done = False
          while not done and steps < 200:
              a = self.choose_action(s)
              s_next, r, done = env.step(a)
              if visual_render == True:
                env.render(self.Q)
              self.update(s, a, r, s_next)
              total_r += r; s = s_next; steps += 1
          if hasattr(self, 'average_rewards'):
              self.average_rewards.append(total_r / steps)




