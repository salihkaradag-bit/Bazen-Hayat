package com.mafia.game;

import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.ScreenUtils;

public class MapScreen implements Screen {
    private final Mafia game;
    private Texture map;
    private OrthographicCamera camera;
    private float zoom = 1f;
    private int lastTouchX, lastTouchY;
    private InputAdapter mapInputAdapter;

    public MapScreen(Mafia game) {
        this.game = game;
        map = new Texture("maps/istanbul.png"); // png ise png yapmayı unutma
        camera = new OrthographicCamera();

        // Harita kaydırma ve zoom kontrolleri
        mapInputAdapter = new InputAdapter() {
            @Override
            public boolean scrolled(float amountX, float amountY) {
                zoom += amountY * 0.1f;
                zoom = MathUtils.clamp(zoom, 0.5f, 8f);
                camera.zoom = zoom;
                return true;
            }

            @Override
            public boolean touchDown(int screenX, int screenY, int pointer, int button) {
                lastTouchX = screenX;
                lastTouchY = screenY;
                return true;
            }

            @Override
            public boolean touchDragged(int screenX, int screenY, int pointer) {
                float deltaX = (screenX - lastTouchX) * camera.zoom;
                float deltaY = (screenY - lastTouchY) * camera.zoom;
                camera.translate(-deltaX, deltaY);
                lastTouchX = screenX;
                lastTouchY = screenY;
                return true;
            }
        };
    }
    @Override
    public void show() {
        // Artık sadece ekliyoruz, böylece uiStage (menü) her zaman 1 numaralı öncelikte kalıyor.
        game.inputMultiplexer.addProcessor(mapInputAdapter);
    }

    @Override
    public void hide() {
        // Başka sekmeye geçildiğinde harita kontrollerini devre dışı bırak
        game.inputMultiplexer.removeProcessor(mapInputAdapter);
    }

    private void clampCamera() {
        float cameraHalfWidth = camera.viewportWidth * camera.zoom / 2f;
        float cameraHalfHeight = camera.viewportHeight * camera.zoom / 2f;

        float minX = cameraHalfWidth;
        float maxX = map.getWidth() - cameraHalfWidth;
        float minY = cameraHalfHeight;
        float maxY = map.getHeight() - cameraHalfHeight;

        float clampedX = (maxX < minX) ? map.getWidth() / 2f : MathUtils.clamp(camera.position.x, minX, maxX);
        float clampedY = (maxY < minY) ? map.getHeight() / 2f : MathUtils.clamp(camera.position.y, minY, maxY);

        camera.position.set(clampedX, clampedY, 0);
    }

    @Override
    public void render(float delta) {
        ScreenUtils.clear(0.2f, 0.2f, 0.2f, 1);
        clampCamera();
        camera.update();

        game.batch.setProjectionMatrix(camera.combined);
        game.batch.begin();
        game.batch.draw(map, 0, 0);
        game.batch.end();
    }

    @Override
    public void resize(int width, int height) {
        camera.setToOrtho(false, width, height);
        camera.position.set(map.getWidth() / 2f, map.getHeight() / 2f, 0);
    }

    @Override public void pause() {}
    @Override public void resume() {}
    @Override public void dispose() { map.dispose(); }
}
