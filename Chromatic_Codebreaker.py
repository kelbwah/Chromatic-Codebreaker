import import_handler as shared
import game_screen, home_screen, how_to_play

HomeScreen = home_screen.HomeScreen()
GameScreen = game_screen.GameScreen()
HowToPlayScreen = how_to_play.HowToPlayScreen()



def main():
    current_screen = HomeScreen
    while True:

        #Drawing and updating screens
        current_screen.draw()
        current_screen.update()


        #Handling events for each screen
        for event in shared.pygame.event.get():
            current_screen.handle_event(event)
        
        #Changing screens
        if current_screen.is_done() == True:
            next_screen = current_screen.next_screen
            if next_screen == 'how_to_play_screen':
                current_screen = HowToPlayScreen
                current_screen.screen_done = False
            elif next_screen == 'home_screen':
                current_screen = HomeScreen
                current_screen.screen_done = False
            elif next_screen == 'game_screen':
                current_screen = GameScreen
                current_screen.screen_done = False

        shared.pygame.display.flip()
        shared.clock.tick(60)

if __name__ == '__main__':
    main()