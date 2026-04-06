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

public class TravelScreen implements Screen {
    private final Mafia game;
    private Stage stage;
    private BitmapFont font;

    public TravelScreen(Mafia game) {
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

        Label.LabelStyle titleStyle = new Label.LabelStyle(font, Color.CYAN);
        TextButton.TextButtonStyle btnStyle = new TextButton.TextButtonStyle();
        btnStyle.font = font;
        btnStyle.up = createSolidBackground(Color.DARK_GRAY);
        btnStyle.down = createSolidBackground(Color.LIGHT_GRAY);

        Label titleLabel = new Label("--- SEYAHAT ACENTESI ---", titleStyle);
        TextButton goAnkaraBtn = new TextButton("Ankara'ya Uc", btnStyle);
        TextButton goIzmirBtn = new TextButton("Izmir'e Uc", btnStyle);

        table.add(titleLabel).padBottom(50).row();
        table.add(goAnkaraBtn).size(250, 60).pad(10).row();
        table.add(goIzmirBtn).size(250, 60).pad(10).row();

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
        ScreenUtils.clear(0.05f, 0.1f, 0.2f, 1); // Gece Mavisi
        stage.act(delta);
        stage.draw();
    }
    @Override public void resize(int width, int height) { stage.getViewport().update(width, height, true); }
    @Override public void pause() {}
    @Override public void resume() {}
    @Override public void dispose() { stage.dispose(); font.dispose(); }
}
