package com.mafia.game;

import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputMultiplexer;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;

public class Mafia extends Game {
    public SpriteBatch batch;
    public Stage uiStage;
    public InputMultiplexer inputMultiplexer;

    // Ekranlarımız
    private MapScreen mapScreen;
    private MoneyScreen moneyScreen;
    private GunScreen gunScreen;
    private TravelScreen travelScreen;
    private ProfileScreen menuScreen;

    @Override
    public void create() {
        batch = new SpriteBatch();
        uiStage = new Stage(new ScreenViewport(), batch);

        inputMultiplexer = new InputMultiplexer();
        inputMultiplexer.addProcessor(uiStage); // UI olayları daima öncelikli
        Gdx.input.setInputProcessor(inputMultiplexer);

        // Ekranları başlat
        mapScreen = new MapScreen(this);
        moneyScreen = new MoneyScreen(this);
        gunScreen = new GunScreen(this);
        travelScreen = new TravelScreen(this);
        menuScreen = new ProfileScreen(this);

        createCircularBottomMenu();

        // Harita ile başlat
        setScreen(mapScreen);
    }

    private void createCircularBottomMenu() {
        Table bottomTable = new Table();
        bottomTable.setFillParent(true);
        bottomTable.bottom();
        bottomTable.padBottom(20);

        Texture circleTexture = generateCircleTexture(100);
        Drawable circleBackground = new TextureRegionDrawable(circleTexture);
        Drawable circleBackgroundOver = new TextureRegionDrawable(circleTexture).tint(new Color(0.8f, 0.8f, 0.8f, 1f));

        TextButton.TextButtonStyle style = new TextButton.TextButtonStyle();
        style.up = circleBackground;
        style.over = circleBackgroundOver;
        style.down = circleBackgroundOver;
        style.font = new BitmapFont();
        style.fontColor = Color.CLEAR;

        // 5 Sekmeyi Oluştur
        addCircularTab(bottomTable, "ui/mainpage.jpg", mapScreen, style);
        addCircularTab(bottomTable, "ui/moneypage.jpg", moneyScreen, style);
        addCircularTab(bottomTable, "ui/gunpage.jpg", gunScreen, style);
        addCircularTab(bottomTable, "ui/travelpage.jpg", travelScreen, style);
        addCircularTab(bottomTable, "ui/menupage.jpg", menuScreen, style);

        uiStage.addActor(bottomTable);
    }

    // TEK BİR METOD TÜM EKRANLAR İÇİN YETERLİ (Hata veren log silindi)
    private void addCircularTab(Table table, String iconPath, final Screen targetScreen, TextButton.TextButtonStyle style) {
        Texture iconTexture = new Texture(iconPath);
        Image iconImage = new Image(iconTexture);
        iconImage.setScaling(Scaling.fit);

        // İkonun tıklama algılamasını kapat (Tıklama içinden geçsin)
        iconImage.setTouchable(Touchable.disabled);

        Stack stack = new Stack();
        TextButton button = new TextButton("", style);

        Container<Image> iconContainer = new Container<Image>(iconImage);
        iconContainer.size(60, 60);
        iconContainer.center();

        // Konteynerin de tıklama algılamasını kapat
        iconContainer.setTouchable(Touchable.disabled);

        stack.add(button);
        stack.add(iconContainer);

        // Tıklamayı direkt Butona veriyoruz
        button.addListener(new ClickListener() {
            public void clicked(InputEvent event, float x, float y) {
                setScreen(targetScreen); // Ekranı değiştir!
            }
        });

        table.add(stack).size(100, 100).pad(15);
    }

    private Texture generateCircleTexture(int size) {
        Pixmap pixmap = new Pixmap(size, size, Pixmap.Format.RGBA8888);
        pixmap.setColor(1, 1, 1, 1);
        pixmap.fillCircle(size / 2, size / 2, size / 2);
        Texture texture = new Texture(pixmap);
        pixmap.dispose();
        return texture;
    }

    @Override
    public void render() {
        super.render();
        uiStage.act(Gdx.graphics.getDeltaTime());
        uiStage.draw();
    }

    @Override
    public void dispose() {
        batch.dispose();
        uiStage.dispose();
        if(screen != null) screen.dispose();
    }
}
