import sys
import pygame
import qlearning_agent
import new_grid
#import grid
import new_random_agent


clock = pygame.time.Clock()

def main():
    qLearning_sim = False
    visual_render = False
    playing = True
    
    if qLearning_sim == False :
        grid_env = new_grid.Grid(6, 6, obstacles=[(1,1), (4,1)])
        r_agent = new_random_agent.RandomAgent()
        r_agent.run(grid_env)

    else:
        grid_env = new_grid.Grid(6, 6, obstacles=[(1,1), (4,1)])
        q_agent = qlearning_agent.QLearningAgent(6 * 6)
    
        q_agent.train(grid_env,visual_render)
    
        # Run a demonstration
        s = grid_env.reset()
        for _ in range(10):
            grid_env.render(q_table=q_agent.Q,delay = 0.03)
            s, r, done = grid_env.step(q_agent.choose_action(s, greedy=True))
            if done: break
        q_agent.plot_reward_curves()
        pygame.quit()
        

    


    
if __name__ == "__main__":    
    main()

    pygame.quit()
    sys.exit()




#if QLearningSim == "False":   
       # grid1 = grid.Grid()
        #grid1.drawGrid()
        #myAgent = random_agent.RandomAgent(grid1.screen,grid1.startX,grid1.startY,grid1.singleGridWidth)
        #pygame.display.flip()
        #Failed implementation 
        #myAgent.run(grid1,myAgent)
        #while playing:
         #   for event in pygame.event.get():
          #      if event.type == pygame.QUIT:
           #         playing = False
        
            #clock.tick(60)