import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.ai_settings=ai_settings
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        # self.image = pygame.transform.rotate(pygame.image.load('ship.bmp'),-90)
        self.image = pygame.image.load('ship.bmp')
        print(self.image.get_rect())
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # #将每搜飞船放在屏幕左侧中央
        # self.rect.left = self.screen_rect.left
        # self.rect.centery = self.screen_rect.centery


        self.center=float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)
        # self.left=float(self.rect.left)
        # self.centery=float(self.rect.centery)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
            # self.left += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
            # self.left -= self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.centerx < self.screen_rect.centerx:
        if self.moving_up and self.rect.bottom >self.image.get_height():
            self.bottom-=self.ai_settings.ship_speed_factor
            # self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
            # self.centery += self.ai_settings.ship_speed_factor
        #
        self.rect.centerx=self.center
        self.rect.bottom=self.bottom

        # self.rect.left = self.left
        # self.rect.centery=self.centery


    def blitme(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        self.center=self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
