import java.io.IOException;
import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.MidiUnavailableException;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;

/**
 * An implementation of a sound processor that is able to play midi files.
 */
public class AudioPlayer {
	/**
	 * The AudioPlayer class creates an object that reads midi files.
	 */
	private Sequence sequence;
	private String songName;
	private Sequencer sequencer;

	/**
	 * Create a AudioPlayer and initiate necessary components for playing the
	 * file.
	 * 
	 * @param song
	 *            : the song that is going to be played by the player.
	 * 
	 * @throws MidiUnavailableException
	 *             , InvalidMidiDataException, IOException, NullPointerException
	 */
	public AudioPlayer(Object song) throws MidiUnavailableException,
			InvalidMidiDataException, IOException, NullPointerException {
		// initialize sequence and sequencer for song
		sequence = MidiSystem.getSequence(((Song) song).getSource());
		songName = ((Song) song).getTitle();
		sequencer = MidiSystem.getSequencer();
	}

	/**
	 * plays the midi file and display the title of the song.
	 * 
	 * @throws MidiUnavailableException
	 *             , InvalidMidiDataException
	 */
	public void play() throws MidiUnavailableException,
			InvalidMidiDataException {
		// open and start playing sequencer
		sequencer.open();
		sequencer.setSequence(sequence);
		sequencer.start();
		System.out.println("Playing " + songName + "...");

	}

	/**
	 * Check to see if the player is still playing music.
	 */
	public void checkIfRunning() {
		// check every second to see if the song is still playing
		while (true) {
			if (sequencer.isRunning()) {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException ignore) {
					break;
				}
			} else {
				break;
			}
		}
	}

	/**
	 * Close the sequencer that is playing.
	 */
	public void close() {
		// stop the music from playing
		sequencer.close();
	}

	/**
	 * Pause the sequencer that is playing.
	 */
	public void pause() {
		sequencer.stop();
	}

	/**
	 * Resume the sequencer from the point it was paused.
	 */
	public void resume() {
		sequencer.start();
	}
}