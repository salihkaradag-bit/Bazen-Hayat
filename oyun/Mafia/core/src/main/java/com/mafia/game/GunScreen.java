package com.mafia.game;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.ScreenViewport;

public class GunScreen implements Screen {
    private final Mafia game;
    private Stage stage;
    private BitmapFont font;

    public GunScreen(Mafia game) {
        this.game = game;
        stage = new Stage(new ScreenViewport(), game.batch);
        font = new BitmapFont();
        font.getData().setScale(1.5f);
        setupUI();
    }

    private void setupUI() {
        Table table = new Table();
        table.setFillParent(true);
        table.top().padTop(80);

        Label.LabelStyle titleStyle = new Label.LabelStyle(font, Color.RED);
        TextButton.TextButtonStyle btnStyle = new TextButton.TextButtonStyle();
        btnStyle.font = font;
        btnStyle.up = createSolidBackground(Color.DARK_GRAY);
        btnStyle.down = createSolidBackground(Color.LIGHT_GRAY);

        Label titleLabel = new Label("--- MAFYATIK ISLER ---", titleStyle);
        TextButton buyGunBtn = new TextButton("Kelesnikof Al ($15.000)", btnStyle);
        TextButton hireGoonBtn = new TextButton("Tetikci Tut ($5.000)", btnStyle);

        table.add(titleLabel).padBottom(50).row();
        table.add(buyGunBtn).size(300, 60).pad(10).row();
        table.add(hireGoonBtn).size(300, 60).pad(10).row();

        stage.addActor(table);
    }

    private TextureRegionDrawable createSolidBackground(Color color) {
        Pixmap pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888);
        pixmap.setColor(color);
        pixmap.fill();
        Texture texture = new Texture(pixmap);
        pixmap.dispose();
        return new TextureRegionDrawable(texture);
    }

    @Override public void show() { game.inputMultiplexer.addProcessor(stage); }
    @Override public void hide() { game.inputMultiplexer.removeProcessor(stage); }
    @Override public void render(float delta) {
        ScreenUtils.clear(0.2f, 0.05f, 0.05f, 1); // Koyu Kırmızı
        stage.act(delta);
        stage.draw();
    }
    @Override public void resize(int width, int height) { stage.getViewport().update(width, height, true); }
    @Override public void pause() {}
    @Override public void resume() {}
    @Override public void dispose() { stage.dispose(); font.dispose(); }
}
