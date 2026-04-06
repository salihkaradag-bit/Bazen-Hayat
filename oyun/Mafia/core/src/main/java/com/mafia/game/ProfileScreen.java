package com.mafia.game;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.ScreenViewport;

public class ProfileScreen implements Screen {
    private final Mafia game;
    private Stage stage;
    private BitmapFont font;

    public ProfileScreen(Mafia game) {
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

        Label.LabelStyle titleStyle = new Label.LabelStyle(font, Color.MAGENTA);
        Label.LabelStyle infoStyle = new Label.LabelStyle(font, Color.WHITE);

        Label titleLabel = new Label("--- KARAKTER PROFILI ---", titleStyle);
        Label nameLabel = new Label("Isim: Don Corleone", infoStyle);
        Label repLabel = new Label("Sayginlik: %85", infoStyle);
        Label levelLabel = new Label("Seviye: 12 (Babalarin Babasi)", infoStyle);

        table.add(titleLabel).padBottom(40).row();
        table.add(nameLabel).padBottom(20).row();
        table.add(repLabel).padBottom(20).row();
        table.add(levelLabel).padBottom(20).row();

        stage.addActor(table);
    }

    @Override public void show() { game.inputMultiplexer.addProcessor(stage); }
    @Override public void hide() { game.inputMultiplexer.removeProcessor(stage); }
    @Override public void render(float delta) {
        ScreenUtils.clear(0.15f, 0.05f, 0.15f, 1); // Koyu Mor
        stage.act(delta);
        stage.draw();
    }
    @Override public void resize(int width, int height) { stage.getViewport().update(width, height, true); }
    @Override public void pause() {}
    @Override public void resume() {}
    @Override public void dispose() { stage.dispose(); font.dispose(); }
}
