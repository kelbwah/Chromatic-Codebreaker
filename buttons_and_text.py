import import_handler as shared

class ButtonsAndText:
    def __init__(self):
        self.screen = shared.screen

    def add_instructions_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 64)
        title_text = font.render('Instructions', True, shared.black)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (shared.screen_width/2, 75)
        shared.screen.blit(title_text, title_text_rect)

        other_font = shared.pygame.font.Font('gaming_font.ttf', 48)
        instructions_text_1 = other_font.render('The goal of the game is to guess a random computer', True, shared.black)
        instructions_text_rect_1 = instructions_text_1.get_rect()
        instructions_text_rect_1.center = (shared.screen_width/2, 200)
        shared.screen.blit(instructions_text_1, instructions_text_rect_1)
        
        instructions_text_2 = other_font.render('generated color sequence. Change the colors using', True, shared.black)
        instructions_text_rect_2 = instructions_text_2.get_rect()
        instructions_text_rect_2.center = (shared.screen_width/2, 250)
        shared.screen.blit(instructions_text_2, instructions_text_rect_2)

        instructions_text_3 = other_font.render('the up or down arrows and when you\'re ready,', True, shared.black)
        instructions_text_rect_3 = instructions_text_3.get_rect()
        instructions_text_rect_3.center = (shared.screen_width/2, 300)
        shared.screen.blit(instructions_text_3, instructions_text_rect_3)

        instructions_text_4 = other_font.render('press the \'guess\' button. You can play as many', True, shared.black)
        instructions_text_rect_4 = instructions_text_4.get_rect()
        instructions_text_rect_4.center = (shared.screen_width/2, 350)
        shared.screen.blit(instructions_text_4, instructions_text_rect_4)

        instructions_text_5 = other_font.render('times as you want see your highest score! Good luck!', True, shared.black)
        instructions_text_rect_5 = instructions_text_5.get_rect()
        instructions_text_rect_5.center = (shared.screen_width/2, 400)
        shared.screen.blit(instructions_text_5, instructions_text_rect_5)

        instructions_text_6 = other_font.render('NIS = Not in sequence -- NIP = Not in place -- ICP = In correct place', True, shared.black)
        instructions_text_rect_6 = instructions_text_6.get_rect()
        instructions_text_rect_6.center = (shared.screen_width/2, 500)
        shared.screen.blit(instructions_text_6, instructions_text_rect_6)

    def create_score_text(self, curr_score, best_score):
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        score_text = font.render('Current Tries: ' + str(curr_score) + '\nBest Score: ' + str(best_score), True, shared.black)
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (shared.screen_width-350, 50)
        shared.screen.blit(score_text, score_text_rect)

    def create_title_text(self):

        font = shared.pygame.font.Font('gaming_font.ttf', 132)
        text = font.render('Chromatic Codebreaker', True, shared.black)
        text_rect = text.get_rect()
        text_rect.center = (shared.screen_width/2, shared.screen_height/4)
        shared.screen.blit(text, text_rect)

        other_font = shared.pygame.font.Font('gaming_font.ttf', 26)
        bottom_text = other_font.render('Try To Guess The Sequence!', True, shared.black)
        bottom_text_rect = bottom_text.get_rect()
        bottom_text_rect.center = (shared.screen_width/2, shared.screen_height/2.5)
        self.screen.blit(bottom_text, bottom_text_rect)

    def create_no_sequence_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        text = font.render('No Sequence Yet, Click \nNew Sequence Button', True, shared.black)
        text_rect = text.get_rect()
        text_rect.topleft = (40.5, 50)
        shared.screen.blit(text, text_rect)

    def create_has_sequence_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 36)
        text = font.render('New code set.\nNIP = Not in place\nNIS = Not in sequence\nICP = In correct place', True, shared.black)
        text_rect = text.get_rect()
        text_rect.topleft = (65, 45)
        shared.screen.blit(text, text_rect)
    
    def create_NIP_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 28)
        text = font.render('NIP', True, shared.black)
        text_rect = text.get_rect()
        return (text, text_rect)

    def create_NIS_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 28)
        text = font.render('NIS', True, shared.black)
        text_rect = text.get_rect()
        return (text, text_rect)
    
    def create_ICP_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 28)
        text = font.render('ICP', True, shared.black)
        text_rect = text.get_rect()
        return (text, text_rect)

    def create_hints_text(self, guess_outcome):
        if guess_outcome[0] == 'NIP':
            text1, text_rect1 = self.create_NIP_text()
            text_rect1.center = (shared.screen_width/7, shared.screen_height/2.55)
            shared.screen.blit(text1, text_rect1)
        if guess_outcome[1] == 'NIP':
            text2, text_rect2 = self.create_NIP_text()
            text_rect2.center = (shared.screen_width/3.4, shared.screen_height/2.55)
            shared.screen.blit(text2, text_rect2)
        if guess_outcome[2] == 'NIP':
            text3, text_rect3 = self.create_NIP_text()
            text_rect3.center = (shared.screen_width/2.3, shared.screen_height/2.55)
            shared.screen.blit(text3, text_rect3)
        if guess_outcome[3] == 'NIP':
            text4, text_rect4 = self.create_NIP_text()
            text_rect4.center = (shared.screen_width/1.73, shared.screen_height/2.55)
            shared.screen.blit(text4, text_rect4)
        if guess_outcome[4] == 'NIP':
            text5, text_rect5 = self.create_NIP_text()
            text_rect5.center = (shared.screen_width/1.4, shared.screen_height/2.55)
            shared.screen.blit(text5, text_rect5)
        if guess_outcome[5] == 'NIP':
            text6, text_rect6 = self.create_NIP_text()
            text_rect6.center = (shared.screen_width * 6 / 7, shared.screen_height/2.55)
            shared.screen.blit(text6, text_rect6)
        #-----------------------------------------------------------------------#
        #-----------------------------------------------------------------------#
        if guess_outcome[0] == 'NIS':
            text1, text_rect1 = self.create_NIS_text()
            text_rect1.center = (shared.screen_width/7, shared.screen_height/2.55)
            shared.screen.blit(text1, text_rect1)
        if guess_outcome[1] == 'NIS':
            text2, text_rect2 = self.create_NIS_text()
            text_rect2.center = (shared.screen_width/3.4, shared.screen_height/2.55)
            shared.screen.blit(text2, text_rect2)
        if guess_outcome[2] == 'NIS':
            text3, text_rect3 = self.create_NIS_text()
            text_rect3.center = (shared.screen_width/2.3, shared.screen_height/2.55)
            shared.screen.blit(text3, text_rect3)
        if guess_outcome[3] == 'NIS':
            text4, text_rect4 = self.create_NIS_text()
            text_rect4.center = (shared.screen_width/1.73, shared.screen_height/2.55)
            shared.screen.blit(text4, text_rect4)
        if guess_outcome[4] == 'NIS':
            text5, text_rect5 = self.create_NIS_text()
            text_rect5.center = (shared.screen_width/1.4, shared.screen_height/2.55)
            shared.screen.blit(text5, text_rect5)
        if guess_outcome[5] == 'NIS':
            text6, text_rect6 = self.create_NIS_text()
            text_rect6.center = (shared.screen_width * 6 / 7, shared.screen_height/2.55)
            shared.screen.blit(text6, text_rect6)
        #-----------------------------------------------------------------------#
        #-----------------------------------------------------------------------#
        if guess_outcome[0] == 'ICP':
            text1, text_rect1 = self.create_ICP_text()
            text_rect1.center = (shared.screen_width/7, shared.screen_height/2.55)
            shared.screen.blit(text1, text_rect1)
        if guess_outcome[1] == 'ICP':
            text2, text_rect2 = self.create_ICP_text()
            text_rect2.center = (shared.screen_width/3.4, shared.screen_height/2.55)
            shared.screen.blit(text2, text_rect2)
        if guess_outcome[2] == 'ICP':
            text3, text_rect3 = self.create_ICP_text()
            text_rect3.center = (shared.screen_width/2.3, shared.screen_height/2.55)
            shared.screen.blit(text3, text_rect3)
        if guess_outcome[3] == 'ICP':
            text4, text_rect4 = self.create_ICP_text()
            text_rect4.center = (shared.screen_width/1.73, shared.screen_height/2.55)
            shared.screen.blit(text4, text_rect4)
        if guess_outcome[4] == 'ICP':
            text5, text_rect5 = self.create_ICP_text()
            text_rect5.center = (shared.screen_width/1.4, shared.screen_height/2.55)
            shared.screen.blit(text5, text_rect5)
        if guess_outcome[5] == 'ICP':
            text6, text_rect6 = self.create_ICP_text()
            text_rect6.center = (shared.screen_width * 6 / 7, shared.screen_height/2.55)
            shared.screen.blit(text6, text_rect6)
        
    def create_win_text(self):
        font = shared.pygame.font.Font('gaming_font.ttf', 132)
        text = font.render('YOU WIN!', True, shared.black)
        text_rect = text.get_rect()
        text_rect.center = (shared.screen_width/2, shared.screen_height/2)
        shared.screen.blit(text, text_rect)

    def create_retry_button(self):
        self.retry_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/6, 310, 75)
        self.retry_button = shared.pygame.Rect(shared.screen_width/2 - (300/2), shared.screen_height/6, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.retry_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.retry_button)
        
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.retry_text = font.render('Play Again', True, shared.black)
        self.retry_text_rect = self.retry_text.get_rect()
        self.retry_text_rect.center = self.retry_button.center
        self.screen.blit(self.retry_text, self.retry_text_rect)
    
    def shrink_retry_button(self):
        self.retry_button_shade = shared.pygame.Rect(shared.screen_width/2 - (290/2), shared.screen_height/6, 300, 65)
        self.retry_button = shared.pygame.Rect(shared.screen_width/2 - (290/2), shared.screen_height/6, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.retry_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.retry_button)
        
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.retry_text = font.render('Play Again', True, shared.black)
        self.retry_text_rect = self.retry_text.get_rect()
        self.retry_text_rect.center = self.retry_button.center
        self.screen.blit(self.retry_text, self.retry_text_rect)

    def create_sequence_button(self):
        self.sequence_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2-285, 310, 75)
        self.sequence_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2-285, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.sequence_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.sequence_button)
        
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.sequence_text = font.render('New Sequence', True, shared.black)
        self.sequence_text_rect = self.sequence_text.get_rect()
        self.sequence_text_rect.center = self.sequence_button.center
        self.screen.blit(self.sequence_text, self.sequence_text_rect)

    def shrink_sequence_button(self):
        self.sequence_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2-285, 300, 65)
        self.sequence_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2-285, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.sequence_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.sequence_button)
        
        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.sequence_text = font.render('New Sequence', True, shared.black)
        self.sequence_text_rect = self.sequence_text.get_rect()
        self.sequence_text_rect.center = self.sequence_button.center
        self.screen.blit(self.sequence_text, self.sequence_text_rect)

    def create_guess_button(self):
        self.guess_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+210, 310, 75)
        self.guess_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+210, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.guess_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.guess_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.guess_text = font.render('Guess', True, shared.black)
        self.guess_text_rect = self.guess_text.get_rect()
        self.guess_text_rect.center = self.guess_button.center
        self.screen.blit(self.guess_text, self.guess_text_rect)
    
    def shrink_guess_button(self):
        self.guess_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+210, 300, 65)
        self.guess_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+210, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.guess_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.guess_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 48)
        self.guess_text = font.render('Guess', True, shared.black)
        self.guess_text_rect = self.guess_text.get_rect()
        self.guess_text_rect.center = self.guess_button.center
        self.screen.blit(self.guess_text, self.guess_text_rect)

    def create_play_button(self):
        self.play_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+15, 310, 75)
        self.play_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+15, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.play_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.play_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.play_text = font.render('Play', True, shared.black)
        self.play_text_rect = self.play_text.get_rect()
        self.play_text_rect.center = self.play_button.center
        self.screen.blit(self.play_text, self.play_text_rect)
        
    def shrink_play_button(self):
        self.play_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+15, 300, 65)
        self.play_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/2+15, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.play_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.play_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.play_text = font.render('Play', True, shared.black)
        self.play_text_rect = self.play_text.get_rect()
        self.play_text_rect.center = self.play_button.center
        self.screen.blit(self.play_text, self.play_text_rect)

    def create_how_to_play_button(self):
        self.how_to_play_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.5, 310, 75)
        self.how_to_play_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.5, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.how_to_play_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.how_to_play_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.how_to_play_text = font.render('How To Play', True, shared.black)
        self.how_to_play_text_rect = self.how_to_play_text.get_rect()
        self.how_to_play_text_rect.center = self.how_to_play_button.center
        self.screen.blit(self.how_to_play_text, self.how_to_play_text_rect)

    def shrink_how_to_play_button(self):
        self.how_to_play_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.5, 300, 65)
        self.how_to_play_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.5, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.how_to_play_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.how_to_play_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.how_to_play_text = font.render('How To Play', True, shared.black)
        self.how_to_play_text_rect = self.how_to_play_text.get_rect()
        self.how_to_play_text_rect.center = self.how_to_play_button.center
        self.screen.blit(self.how_to_play_text, self.how_to_play_text_rect)

    def create_exit_button(self):
        self.exit_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.23, 310, 75)
        self.exit_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.23, 300, 65)
        shared.pygame.draw.rect(self.screen, shared.gray, self.exit_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.exit_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.exit_text = font.render('Exit', True, shared.black)
        self.exit_text_rect = self.exit_text.get_rect()
        self.exit_text_rect.center = self.exit_button.center
        self.screen.blit(self.exit_text, self.exit_text_rect)

    def shrink_exit_button(self):
        self.exit_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.23, 300, 65)
        self.exit_button = shared.pygame.Rect(shared.screen_width/2-(300/2), shared.screen_height/1.23, 290, 55)
        shared.pygame.draw.rect(self.screen, shared.gray, self.exit_button_shade)
        shared.pygame.draw.rect(self.screen, shared.coral, self.exit_button)

        font = shared.pygame.font.Font('gaming_font.ttf', 32)
        self.exit_text = font.render('Exit', True, shared.black)
        self.exit_text_rect = self.exit_text.get_rect()
        self.exit_text_rect.center = self.exit_button.center
        self.screen.blit(self.exit_text, self.exit_text_rect)

    def create_return_button(self, check):
        if check == 1:
            self.return_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), (shared.screen_height / 1.2), 310, 75)
            self.return_button = shared.pygame.Rect(shared.screen_width/2-(300/2), (shared.screen_height / 1.2), 300, 65)
            shared.pygame.draw.rect(self.screen, shared.gray, self.return_button_shade)
            shared.pygame.draw.rect(self.screen, shared.coral, self.return_button)

            font = shared.pygame.font.Font('gaming_font.ttf', 32)
            self.return_text = font.render('Return', True, shared.black)
            self.return_text_rect = self.return_text.get_rect()
            self.return_text_rect.center = self.return_button.center
            self.screen.blit(self.return_text, self.return_text_rect)
        elif check == 2:
            self.return_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2) + 400, shared.screen_height / 2 + 210, 310, 75)
            self.return_button = shared.pygame.Rect(shared.screen_width/2-(300/2) + 400, shared.screen_height / 2 + 210, 300, 65)
            shared.pygame.draw.rect(self.screen, shared.gray, self.return_button_shade)
            shared.pygame.draw.rect(self.screen, shared.coral, self.return_button)

            font = shared.pygame.font.Font('gaming_font.ttf', 48)
            self.return_text = font.render('Return', True, shared.black)
            self.return_text_rect = self.return_text.get_rect()
            self.return_text_rect.center = self.return_button.center
            self.screen.blit(self.return_text, self.return_text_rect)

    def shrink_return_button(self, check):
        if check == 1: #return button for how to play screen
            self.return_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2), (shared.screen_height /1.2), 300, 65)
            self.return_button = shared.pygame.Rect(shared.screen_width/2-(300/2), (shared.screen_height / 1.2), 290, 55)
            shared.pygame.draw.rect(self.screen, shared.gray, self.return_button_shade)
            shared.pygame.draw.rect(self.screen, shared.coral, self.return_button)

            font = shared.pygame.font.Font('gaming_font.ttf', 32)
            self.return_text = font.render('Return', True, shared.black)
            self.return_text_rect = self.return_text.get_rect()
            self.return_text_rect.center = self.return_button.center
            self.screen.blit(self.return_text, self.return_text_rect)
        elif check == 2: #return button for game screen
            self.return_button_shade = shared.pygame.Rect(shared.screen_width/2-(300/2) + 400, shared.screen_height / 2 + 210, 300, 65)
            self.return_button = shared.pygame.Rect(shared.screen_width/2-(300/2) + 400, shared.screen_height / 2 + 210, 290, 55)
            shared.pygame.draw.rect(self.screen, shared.gray, self.return_button_shade)
            shared.pygame.draw.rect(self.screen, shared.coral, self.return_button)

            font = shared.pygame.font.Font('gaming_font.ttf', 48)
            self.return_text = font.render('Return', True, shared.black)
            self.return_text_rect = self.return_text.get_rect()
            self.return_text_rect.center = self.return_button.center
            self.screen.blit(self.return_text, self.return_text_rect)

    def create_up_arrow_button(self, x, y):
        up_arrow = shared.up_arrow
        up_arrow_rect = up_arrow.get_rect()
        up_arrow_rect.center = (x,y)
        return up_arrow, up_arrow_rect
    
    def create_down_arrow_button(self, x, y):
        down_arrow = shared.down_arrow
        down_arrow_rect = down_arrow.get_rect()
        down_arrow_rect.center = (x,y)
        return down_arrow, down_arrow_rect
    
    def create_shrinked_up_arrow_button(self, x, y):
        shrinked_up_arrow = shared.shrinked_up_arrow
        shrinked_up_arrow_rect = shrinked_up_arrow.get_rect()
        shrinked_up_arrow_rect.center = (x,y)
        return shrinked_up_arrow, shrinked_up_arrow_rect

    def create_shrinked_down_arrow_button(self, x, y):
        shrinked_down_arrow = shared.shrinked_down_arrow
        shrinked_down_arrow_rect = shrinked_down_arrow.get_rect()
        shrinked_down_arrow_rect.center = (x,y)
        return shrinked_down_arrow, shrinked_down_arrow_rect

    def create_music_play_button(self):
        self.play_music_button = shared.play_music_button
        self.play_music_button_rect = self.play_music_button.get_rect()
        self.play_music_button_rect.center = (95, shared.screen_height-95)
        self.screen.blit(self.play_music_button, self.play_music_button_rect)
    
    def shrink_music_play_button(self):
        self.play_music_button = shared.pygame.transform.scale(shared.play_music_button, (90, 90))
        self.play_music_button_rect = self.play_music_button.get_rect()
        self.play_music_button_rect.center = (95, shared.screen_height-95)
        self.screen.blit(self.play_music_button, self.play_music_button_rect)

    def create_music_pause_button(self):
        self.pause_music_button = shared.pause_music_button
        self.pause_music_button_rect = self.pause_music_button.get_rect()
        self.pause_music_button_rect.center = (95, shared.screen_height-95)
        self.screen.blit(self.pause_music_button, self.pause_music_button_rect)

    def shrink_music_pause_button(self):
        self.pause_music_button = shared.pygame.transform.scale(shared.pause_music_button, (90, 90))
        self.pause_music_button_rect = self.pause_music_button.get_rect()
        self.pause_music_button_rect.center = (95, shared.screen_height-95)
        self.screen.blit(self.pause_music_button, self.pause_music_button_rect)
    
    