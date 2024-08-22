import hashlib
import json

class VotingSystem:
    def __init__(self):
        self.votes = []
        self.voter_hashes = set()  # Track hashed voter IDs to prevent double voting
    
    def hash_vote(self, vote):
        return hashlib.sha256(vote.encode()).hexdigest()

    def cast_vote(self, voter_id, vote):
        # Ensure voter cannot vote more than once
        voter_hash = self.hash_vote(voter_id)
        if voter_hash in self.voter_hashes:
            raise ValueError("Voter has already cast a vote.")
        
        # Cast vote
        self.votes.append({
            'voter_id_hash': voter_hash,
            'vote': vote
        })
        self.voter_hashes.add(voter_hash)
        print("Vote cast successfully.")

    def tally_votes(self):
        # Tally votes without revealing individual voter IDs
        vote_counts = {}
        for entry in self.votes:
            vote = entry['vote']
            if vote in vote_counts:
                vote_counts[vote] += 1
            else:
                vote_counts[vote] = 1
        return vote_counts

    def get_results(self):
        # Print results of the voting
        results = self.tally_votes()
        print("Voting Results:")
        for option, count in results.items():
            print(f"{option}: {count} votes")

# Example usage
def main():
    system = VotingSystem()

    # Simulate voting
    try:
        system.cast_vote('voter1', 'OptionA')
        system.cast_vote('voter2', 'OptionB')
        system.cast_vote('voter1', 'OptionA')  # Should raise an error
        
    except ValueError as e:
        print(e)

    # Print results
    system.get_results()

if __name__ == "__main__":
    main()
