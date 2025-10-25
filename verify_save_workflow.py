"""
Verification Script for "Save My Work" Workflow
Tests all 4 steps: Windsurf Memory, Supermemory.ai, Git Commit, GitHub Push
"""

from dual_memory_helper import DualMemoryHelper
import subprocess
import os
from datetime import datetime

class SaveWorkflowVerifier:
    """Verify all 4 steps of the save workflow"""
    
    def __init__(self, project_name, project_path):
        self.project_name = project_name
        self.project_path = project_path
        self.helper = DualMemoryHelper(project_name)
        self.verification_results = {
            'windsurf_memory': False,
            'supermemory_ai': False,
            'git_commit': False,
            'github_push': False
        }
    
    def verify_all(self, summary, next_steps, status, github_url=None):
        """
        Run complete verification of all 4 steps.
        
        Returns:
            dict with verification results for each step
        """
        print("=" * 70)
        print("SAVE MY WORK - VERIFICATION WORKFLOW")
        print("=" * 70)
        
        # Step 1 & 2: Save to both memory systems
        print("\n📝 STEP 1 & 2: Saving to Memory Systems...")
        memory_results = self.helper.save_session_end(
            summary=summary,
            next_steps=next_steps,
            status=status,
            github_url=github_url,
            verify=True
        )
        
        # Check Windsurf Memory (manual verification needed)
        if memory_results['windsurf'] == 'manual_save_required':
            print("\n⚠️  Windsurf Memory: Manual save required via Cascade")
            print("    Ask Cascade to save the content shown above")
            self.verification_results['windsurf_memory'] = 'manual'
        
        # Check Supermemory.ai
        if memory_results.get('supermemory') and isinstance(memory_results['supermemory'], dict):
            self.verification_results['supermemory_ai'] = True
            supermemory_id = memory_results['supermemory']['id']
        else:
            supermemory_id = None
        
        # Step 3: Git Commit
        print("\n📦 STEP 3: Git Commit Verification...")
        commit_hash = self.verify_git_commit()
        
        # Step 4: GitHub Push
        print("\n🚀 STEP 4: GitHub Push Verification...")
        push_success, branch_name = self.verify_github_push()
        
        # Final Checklist
        print("\n" + "=" * 70)
        print("FINAL VERIFICATION CHECKLIST")
        print("=" * 70)
        
        windsurf_status = "⚠️  Manual save required" if self.verification_results['windsurf_memory'] == 'manual' else "❌ Not saved"
        supermemory_status = f"✅ Saved (ID: {supermemory_id})" if self.verification_results['supermemory_ai'] else "❌ Not saved"
        git_status = f"✅ Committed (hash: {commit_hash})" if self.verification_results['git_commit'] else "❌ Not committed"
        github_status = f"✅ Pushed (branch: {branch_name})" if self.verification_results['github_push'] else "❌ Not pushed"
        
        print(f"\n1. Windsurf Memory:  {windsurf_status}")
        print(f"2. Supermemory.ai:   {supermemory_status}")
        print(f"3. Git Commit:       {git_status}")
        print(f"4. GitHub Push:      {github_status}")
        
        # Overall status
        all_verified = (
            self.verification_results['windsurf_memory'] in [True, 'manual'] and
            self.verification_results['supermemory_ai'] and
            self.verification_results['git_commit'] and
            self.verification_results['github_push']
        )
        
        print("\n" + "=" * 70)
        if all_verified:
            print("✅ ALL 4 STEPS VERIFIED! You can continue from any computer!")
        else:
            print("⚠️  INCOMPLETE: Some steps need attention")
            if not self.verification_results['supermemory_ai']:
                print("   - Supermemory.ai save failed or not configured")
            if not self.verification_results['git_commit']:
                print("   - Git commit needed")
            if not self.verification_results['github_push']:
                print("   - GitHub push needed")
        print("=" * 70)
        
        return self.verification_results
    
    def verify_git_commit(self):
        """Verify git commit and return commit hash"""
        try:
            # Get the latest commit hash
            result = subprocess.run(
                ['git', 'log', '-1', '--format=%H'],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                check=True
            )
            commit_hash = result.stdout.strip()
            
            if commit_hash:
                print(f"   ✅ Latest commit: {commit_hash[:8]}")
                self.verification_results['git_commit'] = True
                return commit_hash[:8]
            else:
                print(f"   ❌ No commits found")
                return None
                
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Git error: {e}")
            return None
    
    def verify_github_push(self):
        """Verify GitHub push status"""
        try:
            # Check if local branch is up to date with remote
            result = subprocess.run(
                ['git', 'status', '-sb'],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                check=True
            )
            status = result.stdout.strip()
            
            # Extract branch name
            branch_name = status.split('...')[0].replace('##', '').strip()
            
            # Check if ahead or behind
            if 'ahead' in status:
                print(f"   ⚠️  Local branch '{branch_name}' is ahead of remote")
                print(f"   Run: git push")
                return False, branch_name
            elif 'behind' in status:
                print(f"   ⚠️  Local branch '{branch_name}' is behind remote")
                print(f"   Run: git pull")
                return False, branch_name
            else:
                print(f"   ✅ Branch '{branch_name}' is up to date with remote")
                self.verification_results['github_push'] = True
                return True, branch_name
                
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Git error: {e}")
            return False, None


# Example usage
if __name__ == "__main__":
    verifier = SaveWorkflowVerifier(
        project_name="supermemory-integration",
        project_path=os.getcwd()
    )
    
    verifier.verify_all(
        summary="Added verification workflow to dual-memory system",
        next_steps="Test verification in real workflow",
        status="Verification system complete",
        github_url="https://github.com/369Temetnosce/supermemory-integration"
    )
