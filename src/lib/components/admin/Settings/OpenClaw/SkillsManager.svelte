<script lang="ts">
  import { onMount } from 'svelte';
  
  export let skills: any[] = [];
  export let loading = false;
  
  let searchQuery = '';
  let filterCategory = 'all';
  
  $: filteredSkills = skills.filter(skill => {
    const matchesSearch = skill.name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          skill.description?.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = filterCategory === 'all' || skill.category === filterCategory;
    return matchesSearch && matchesCategory;
  });
  
  function getCategoryIcon(category: string) {
    switch (category) {
      case 'social': return '📱';
      case 'research': return '🔍';
      case 'automation': return '🤖';
      case 'tools': return '🛠️';
      case 'integration': return '🔗';
      default: return '🧩';
    }
  }
  
  function toggleSkill(skillName: string) {
    // Would call API to toggle
    console.log('Toggle:', skillName);
  }
</script>

<div class="skills-panel">
  <div class="flex items-center justify-between mb-6">
    <h2 class="text-2xl font-bold">🧩 Skills</h2>
    <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
      + Add Skill
    </button>
  </div>
  
  <!-- Search & Filter -->
  <div class="flex gap-3 mb-4">
    <input 
      bind:value={searchQuery}
      type="text" 
      placeholder="Search skills..."
      class="flex-1 px-3 py-2 border rounded-lg bg-white dark:bg-gray-800"
    />
    <select 
      bind:value={filterCategory}
      class="px-3 py-2 border rounded-lg bg-white dark:bg-gray-800"
    >
      <option value="all">All Categories</option>
      <option value="social">Social</option>
      <option value="research">Research</option>
      <option value="automation">Automation</option>
      <option value="tools">Tools</option>
    </select>
  </div>
  
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {#each filteredSkills as skill}
        <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
          <div class="flex items-start justify-between mb-2">
            <div class="flex items-center gap-2">
              <span class="text-2xl">{getCategoryIcon(skill.category)}</span>
              <h3 class="font-semibold">{skill.name || 'Unnamed'}</h3>
            </div>
            <button 
              on:click={() => toggleSkill(skill.name)}
              class="px-2 py-1 text-xs rounded {skill.enabled ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}"
            >
              {skill.enabled ? 'Enabled' : 'Disabled'}
            </button>
          </div>
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">
            {skill.description || 'No description'}
          </p>
          <div class="flex gap-1 flex-wrap">
            {#each skill.tags || [] as tag}
              <span class="px-2 py-0.5 text-xs bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded">
                {tag}
              </span>
            {/each}
          </div>
        </div>
      {/each}
    </div>
    
    {#if filteredSkills.length === 0}
      <div class="text-center py-12 text-gray-500">
        <p class="text-xl mb-2">🧩</p>
        <p>No skills found</p>
      </div>
    {/if}
  {/if}
</div>
